from django.contrib import admin
from userprofile.models import UserProfile, Subscriber
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserProfilerCreationForm, CustomUserChangeForm
from .models import UserProfile

# Register your models here.
# admin.site.register(UserProfile)


class UserProfileAdmin(UserAdmin):
    add_form = UserProfilerCreationForm
    form = CustomUserChangeForm
    model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Subscriber)