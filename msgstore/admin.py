from django.contrib import admin
from .models import msg,information
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ('name','text','ddate')
    ordering = ('ddate',)

admin.site.register(msg,Admin)
admin.site.register(information)