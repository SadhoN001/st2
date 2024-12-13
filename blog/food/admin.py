from django.contrib import admin
from .models import TodoItem, Service
# Register your models here.

admin.site.register(TodoItem)
#dell ABCDef#@

class ServiceAdmin(admin.ModelAdmin):
    list_display= ('service_icon', 'service_title', 'service_des')

admin.site.register(Service, ServiceAdmin)