from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UsersAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_staff')
    list_filter = ('email', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Қол жеткізу құқықтары және растау', {'fields': ('is_staff', 'is_superuser')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')},

         ),
        ('Қол жеткізу құқықтары және растау', {'fields': ('is_staff', 'is_superuser')}),
    )
    search_fields = ('email',)
    ordering = ('email',)




admin.site.register(User, UsersAdmin)
admin.site.register(Logo)