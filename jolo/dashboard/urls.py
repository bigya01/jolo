from django.urls import path
from .views import dashboard_view, location_view, users_view, services_view, billing_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', dashboard_view, name="dashboard"),
    path('', location_view, name="location"),
    path('', users_view, name="users"),
    path('', services_view, name="services"),
    path('', billing_view, name="billing"),
]
