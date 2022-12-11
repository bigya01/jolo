from django.urls import path
from .views import shop_create, service_create, client_register
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('setup/', shop_create, name="setup-shop"),
    path('<slug:shop_slug>/service/create', service_create, name="create-service"),
    path('<slug:shop_slug>/client/register', client_register, name="register-client"),
  
    # path('<slug:shop_slug>/', shop_view, name="shop"),
    # path('<slug:shop_slug>/<slug:service_slug>/', shop_view, name="shop"),
]