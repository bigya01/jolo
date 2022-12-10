from django.db import models
from django.conf import settings
from phone_field import PhoneField    # TODO: pip install django-phone-field


class Shop(models.Model):
    #address from Google API
    shop_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50) # use slugify to populate from shop_name
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
class Service(models.Model):
    service_name = models.CharField(max_length=50)
    duration = models.TimeField()
    shop = models.ForeignKey(Shop, related_name='shop_service', on_delete=models.CASCADE)

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(max_length=254)
    client_phone = PhoneField(blank=True, help_text='Contact phone number')
    # shop = models.ForeignKey(Shop, related_name='shop_client', on_delete=models.CASCADE)


APPOINTMENT_STATUS_CHOICES =(
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Cancelled", "Cancelled"),
)
class Appointment(models.Model):
    appointment_time = models.DateTimeField()
    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS_CHOICES, default="Pending")
    service = models.ForeignKey(Service, related_name='service_appointment', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='shop_appointment', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='client_appointment', on_delete=models.CASCADE)
