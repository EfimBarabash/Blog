from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin


class ProfileInline(admin.TabularInline):
    model = Profile


UserAdmin.inlines = [ProfileInline]

