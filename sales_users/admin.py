from django.contrib import admin
from .models import UserData,ContactData,AccountData
# Register your models here.

admin.site.register(UserData)
admin.site.register(ContactData)
admin.site.register(AccountData)