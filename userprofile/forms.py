from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile

class UserProfilerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserProfile
        fields = ('mobile', )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = UserChangeForm.Meta.fields
