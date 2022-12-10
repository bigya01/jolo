from django.urls import path
from .views import login_view, register_user,setup_shop
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("setup-site/", setup_shop, name="setup")
]
