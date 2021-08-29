from django.contrib import admin
from note_system.models import *
# from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin



# Register your models here.

# @admin.register(User)
# class UserAdmin(DefaultUserAdmin):
#     list_display = ('id','username', 'first_name', 'last_name', 'is_superuser',
#                     'is_staff' ,'is_active',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'theme', 'is_public',
                    'created_at', 'modified_at',)

    list_filter = ('is_public', 'username')

    search_fields = ('username__username', 'theme', 'text', )

    readonly_fields = ('id', 'created_at', 'modified_at',)

