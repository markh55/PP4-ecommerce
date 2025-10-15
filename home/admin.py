from django.contrib import admin
from .models import Subscriber

# Register your models here.
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    readonly_fields = ('date_subscribed',)