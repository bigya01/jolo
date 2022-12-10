from django.contrib import admin
from . import models

@admin.register(models.Shop)
class PostAdmin(admin.ModelAdmin):
    list_display =['shop_name', 'slug', 'user']
    search_fields = ['shop_name', 'user']
    prepopulated_fields = {'slug': ('shop_name',)}

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display =['service_name', 'duration', 'shop']
    search_fields = ['service_name', 'shop']

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display =['client_name', 'client_email', 'client_phone']
    search_fields = ['client_name', 'client_email', 'client_phone']

@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display =['appointment_time', 'appointment_status','choices' ,'service', 'shop', 'client']
    search_fields = ['appointment_time', 'appointment_status', 'choices','service', 'shop', 'client']

