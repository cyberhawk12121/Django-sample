from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Profile

admin.site.register(Profile)
class UserAdmin(BaseUserAdmin):
    list_display= ('email', 'admin')
    list_filter= ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),)
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()    

admin.site.register(CustomUser, UserAdmin)
