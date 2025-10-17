from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order-history/<str:order_number>/', views.order_history, name='order_details'),
]
