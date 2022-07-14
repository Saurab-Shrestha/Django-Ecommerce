from django.urls import path
from .views import start_order
urlpatterns = [
    path('start_order/',start_order,name='start_order'),
    # path('create-checkout-session/', create_checkout_session, name='checkout_session'),
]