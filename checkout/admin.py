from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'full_name', 'email', 'phone_number', 'date', 'order_total')
    ordering = ('-date',)