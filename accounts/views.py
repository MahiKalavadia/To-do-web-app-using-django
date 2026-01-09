from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import ProfileForm
from tasks.models import Task
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from datetime import date, timedelta
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully! You can now login.'
            )
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html')


@login_required
def dashboard_view(request):
    tasks = Task.objects.filter(user=request.user)

    # --- Search ---
    query = request.GET.get('q', '')
    if query:
        tasks = tasks.filter(title__icontains=query)

    # ---Filter ---
    filter_status = request.GET.get('status')
    filter_priority = request.GET.get('priority')
    filter_due = request.GET.get('due')

    today = date.today()

    if filter_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_status == 'pending':
        tasks = tasks.filter(completed=False)

    if filter_priority in ['H', 'M', 'L']:
        tasks = tasks.filter(priority=filter_priority)

    if filter_due == 'today':
        tasks = tasks.filter(due_date=today)
    elif filter_due == 'overdue':
        tasks = tasks.filter(due_date__lt=today, completed=False)
    elif filter_due == 'this_week':
        tasks = tasks.filter(
            due_date__range=[today, today + timedelta(days=7)])

    # ---Sorting---
    sort = request.GET.get('sort')
    if sort == 'asc':
        tasks = tasks.order_by('due_date')
    elif sort == 'desc':
        tasks = tasks.order_by('-due_date')
    else:
        tasks = tasks.order_by('due_date')

    # ---Stats---
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()
    high_priority = tasks.filter(priority='H').count()
    medium_priority = tasks.filter(priority='M').count()
    low_priority = tasks.filter(priority='L').count()

    # ---Pagination---
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tasks': page_obj,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'high_priority': high_priority,
        'medium_priority': medium_priority,
        'low_priority': low_priority,
        'today': today,
        'query': query,
        'filter_status': filter_status,
        'filter_priority': filter_priority,
        'filter_due': filter_due,
        'sort': sort,
    }

    return render(request, 'dashboard.html', context)


@login_required
def set_theme(request, theme):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    
    if theme in ['light','dark']:
        response.set_cookie(
            key='theme',
            value=theme,
            max_age = 60 * 60 * 24 * 30,  # 30 days
            samesite='Lax'
        )
    return response
        

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})


@login_required
def edit_profile(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'edit_profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
