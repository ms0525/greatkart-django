from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone_number')
    readonly_fields = ('date_joined', 'last_login', 'password')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
# Register your models here.

admin.site.register(Account, AccountAdmin)