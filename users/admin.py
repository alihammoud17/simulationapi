from django.contrib import admin
from .models import SiteUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = SiteUser
    search_fields = ('email', 'user_name', 'first_name', 'phone_number')
    list_filter = ('email', 'user_name', 'first_name',
                   'phone_number', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'id', 'user_name', 'first_name', 'phone_number',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Groups', {'fields': ('groups',)}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        SiteUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'phone_number', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(SiteUser, UserAdminConfig)
