from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Usuarios.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Registra el modelo User con el administrador personalizado
admin.site.register(User, CustomUserAdmin)
