from django.contrib import admin

from example.models import UserInformation


@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'ico']
