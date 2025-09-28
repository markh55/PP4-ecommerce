from django.contrib import admin
from .models import Package
from .models import Package, Review, Rating

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'price', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at', 'updated_at', 'tier')
    search_fields = ('name', 'description')
    ordering = ('tier',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'package', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'body', 'user__username', 'package__name')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('package', 'user', 'rating', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'rating')
    search_fields = ('user__username', 'package__name')
    ordering = ('-created_at',)
