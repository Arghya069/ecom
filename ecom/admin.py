from django.contrib import admin
from .models import product,UserManager,User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdminConfig(UserAdmin):

    model = User
    search_fields = ('mobile','Email',
    'first_name','last_name')
    list_filter = ('is_superuser','is_active','is_staff')
    ordering = ('-date_joined',)
    list_display = ('mobile','Email',
    'first_name','last_name','is_active','is_staff')
    fieldsets = (
        (None,{'fields':('mobile','Email','password')}),
        ('details',{'fields':('first_name','last_name','photo')}),
        ('Permissions',{'fields':('is_staff','is_active','is_superuser','groups')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('mobile','Email','first_name','last_name','password1','password2','is_active','is_staff')}),
            )
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['is_staff'].disabled = True

        return form
admin.site.register(product)