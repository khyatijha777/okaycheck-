'''imports'''
from django.contrib import admin
from login.models import Login
class LoginAdmin(admin.ModelAdmin):
    list_display = ['u_id', 'first_name', 'last_name', 'user_name']
    list_display_links = ['u_id', 'first_name', 'user_name']
    list_filter = ['user_name']
# Register your models here.

admin.site.register(Login, LoginAdmin)
