from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from accounts.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ('id','username', 'first_name', 'last_name', 'is_superuser',
                    'is_staff' ,'is_active',)
