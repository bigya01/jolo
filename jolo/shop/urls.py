from django.urls import path
from .views import shop_create, service_create, client_register, appointment_register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('setup/', shop_create, name="setup-shop"),
    path('<slug:shop_slug>/service/create', service_create, name="create-service"),
    path('<slug:shop_slug>/client/register', client_register, name="register-client"),
    path('<slug:shop_slug>/<int:client_id>/<slug:sservice_slug>/appointment', service_create, name="register-appointment"),
    # path('<slug:shop_slug>/', shop_view, name="shop"),
    # path('<slug:shop_slug>/<slug:service_slug>/', shop_view, name="shop"),
]