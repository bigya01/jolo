from django import forms
from django.utils.text import slugify
from .models import Shop, Service, Client, Appointment


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('shop_name', 'address', 'phone')

    # Overriding save function to add slug
    def save(self, *args, **kwargs):   
        # shop = super(ShopCreateForm, self).save(commit=False)
        # shop.shop_slug = slugify(shop.shop_name)
        # if commit:
        #     shop.save()
        # return shop
        
        self.slug = slugify(self.shop_name, instance=self)
        try:
            shop_with_slug_name = Shop.objects.get(slug=self.slug)
        except Shop.DoesNotExist:
            raise forms.ValidationError("Shop name already exists. Please insert a new name!")          
        super().save( *args, **kwargs)

class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('service_name', 'duration')

class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'client_email', 'client_phone')

class AppointmentRegisterForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_time', 'appointment_status')