from django.urls import path
from .views import dashboard_view, location_view, users_view, services_view, billing_view, target_view


urlpatterns = [
    path('<slug:shop_slug>', dashboard_view, name="dashboard"),
    path('<slug:shop_slug>/map/', location_view, name="location"),
    path('<slug:shop_slug>/users/', users_view, name="users"),
    path('<slug:shop_slug>/services/', services_view, name="services"),
    path('<slug:shop_slug>/billing/', billing_view, name="billing"),
    path('<slug:shop_slug>/target/', target_view, name="target"),

]
