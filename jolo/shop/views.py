from django.shortcuts import render, redirect
from .forms import ShopCreateForm, ServiceCreateForm, ClientRegisterForm, AppointmentRegisterForm # TODO

def shop_create(request):
    if request.method == 'POST':
        form = ShopCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_list')
    else:
        form = ShopCreateForm()
        return render(request, 'shop/shop_create.html', {'form': form})

def service_create(request):
    if request.method == 'POST':
        form = ServiceCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceCreateForm()
        return render(request, 'service/service_create.html', {'form': form})


# CLIENT
def client_register(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientRegisterForm()
        return render(request, 'client/client_register.html', {'form': form})

def appointment_register(request):
    if request.method == 'POST':
        form = AppointmentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentRegisterForm()
        return render(request, 'appointment/appointment_register.html', {'form': form})