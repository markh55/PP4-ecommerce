from django.urls import path
from . import views

app_name = 'packages'

urlpatterns = [
    path('', views.package_list, name='package_list'),
    path('tier/<int:tier>/', views.package_list, name='package_list_by_tier'),
    path('<slug:slug>/', views.package_detail, name='package_detail'),
    path('<slug:slug>/review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
]