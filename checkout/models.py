from django.db import models
from django.contrib.auth.models import User
from packages.models import Package

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    business_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_contact_method = models.CharField(max_length=10, blank=True)
    preferred_contact_time = models.CharField(max_length=10, blank=True)
    additional_notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.first_name} {self.surname}"


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lineitems')
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.package.name}"