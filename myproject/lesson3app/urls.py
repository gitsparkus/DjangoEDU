from django.urls import path
from .views import client_orders, client_goods


urlpatterns = [
    path('clientorders/<int:client_id>', client_orders, name='orders'),
    path('clientgoods/<int:client_id>/<int:days>', client_goods, name='orders'),
]
