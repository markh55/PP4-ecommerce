from django.urls import path
from . import views

app_name = 'bag'

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:items_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<int:items_id>/', views.remove_from_bag, name='remove_from_bag'),
]
