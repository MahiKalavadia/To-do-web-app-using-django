from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

        widgets = {
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'})
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']
