from django.urls import path
from .views import appointment_register, shop_view, client_register


urlpatterns = [
    path('<slug:shop_slug>/', shop_view, name="shop"),
    path("<slug:shop_slug>/<slug:service_slug>/client/register/",client_register, name="client_register" ),
     # return redirect(f"{shop_slug}/{service_slug}/{user_id}/appointment_register/")
     path("<slug:shop_slug>/<slug:service_slug>/<int:client_id>/appointment/register/",appointment_register, name="appointment_register" ),

]
