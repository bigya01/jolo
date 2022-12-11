from django.db import models
from django.conf import settings
from phone_field import PhoneField  # TODO: pip install django-phone-field
from datetime import datetime

class Shop(models.Model):
    #address from Google API
    shop_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50) # use slugify to populate from shop_name
    address = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.shop_name
    
    
class Service(models.Model):
    service_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50) # use slugify to populate from shop_name
    duration = models.PositiveIntegerField()
    cost = models.IntegerField()
    shop = models.ForeignKey(Shop, related_name='shop_service', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.service_name
    

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(max_length=254)
    client_phone = PhoneField(blank=True, help_text='Contact phone number')
    
    def __str__(self):
        return self.client_name
    # shop = models.ForeignKey(Shop, related_name='shop_client', on_delete=models.CASCADE)


APPOINTMENT_STATUS_CHOICES =(
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Cancelled", "Cancelled"),
)

TIME_CHOICES = (
    ("10 AM", "10 AM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Appointment(models.Model):
    appointment_time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS_CHOICES, default="Pending")
    service = models.ForeignKey(Service, related_name='service_appointment', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='shop_appointment', on_delete=models.CASCADE)
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    client = models.ForeignKey(Client, related_name='client_appointment', on_delete=models.CASCADE)
    
    def __str__(self):
        service = Service.objects.get(id = self.service_id)

        return f"Appointment {service.service_name} on {self.appointment_time}"
