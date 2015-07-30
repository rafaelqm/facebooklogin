from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'username', 'gender', 'birthdate']

admin.site.register(User, UserAdmin)
