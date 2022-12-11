from django.urls import path
from .views import shop_view


urlpatterns = [
    path('<slug:shop_slug>/', shop_view, name="shop"),
]
