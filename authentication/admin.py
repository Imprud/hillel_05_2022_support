from django.contrib import admin

from .models import Role, User

# Register your models here.
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields: list[str] = ["password"]
    exclude: list[str] = ["user_permissions", "groups"]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
