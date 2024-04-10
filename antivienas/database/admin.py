from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'birthday', 'profile_type', 'wallet')
    search_fields = ('first_name', 'last_name', 'email', 'pk')

admin.site.register(User, UserAdmin)