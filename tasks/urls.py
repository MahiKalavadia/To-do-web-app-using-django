from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('toggle/<int:id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]
