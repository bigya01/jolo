from django import forms
from django.utils.text import slugify
from .models import Shop, Service, Client, Appointment


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('shop_name', 'address', 'phone')

    # Overriding save function to add slug
    def save(self, user_id):   
        shop = super(ShopCreateForm, self).save(commit=False)
        shop.slug = slugify(shop.shop_name)
        shop.user_id = user_id
        shop.save()
        return shop
        
        # self.slug = slugify(self.shop_name, instance=self)
        # if Shop.objects.filter(slug=self.slug).exists():
        #     raise forms.ValidationError("Shop already exists. Please insert a new name!")
        # return super().save( *args, **kwargs)

class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('service_name', 'duration')

    def save(self, shop_slug):
        service = super(ServiceCreateForm, self).save(commit=False)

        service.slug = slugify(service.shop_name)
        if Shop.objects.filter(slug=self.slug).exists():
            raise forms.ValidationError("Service already exists. Please insert a new name!")
        
        if Shop.objects.filter(slug=shop_slug).exists():
            raise forms.ValidationError("Shop does not exist!")
            
        shop = Shop.objects.get(slug=shop_slug)
        service.shop_id = shop.id

        service.save()
        return service

class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'client_email', 'client_phone')

class AppointmentRegisterForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_time', 'appointment_status')

    def save(self, client_id, shop_slug, service_slug):
        appointment = super(AppointmentRegisterForm, self).save(commit=False)
        
        if Client.objects.filter(id = client_id).exists():
            raise forms.ValidationError("User is not registered!")
        if Shop.objects.filter(slug=shop_slug).exists():
            raise forms.ValidationError("Shop does not exist!")
        if Service.objects.filter(slug=service_slug).exists():
            raise forms.ValidationError("Service does not exist!")

        shop = Shop.objects.get(slug=shop_slug)
        appointment.shop_id = shop.id

        service = Service.objects.get(slug=service_slug)
        appointment.service_id = service.id

        appointment.client_id = client_id
    
        appointment.save()
        return appointment