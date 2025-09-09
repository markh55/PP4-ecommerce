from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'price', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at', 'updated_at', 'tier')
    search_fields = ('name', 'description')
    ordering = ('tier',)
