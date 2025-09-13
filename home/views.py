from django.shortcuts import render
from packages.models import Package

# Create your views here.
def index(request):
    packages = Package.objects.all()[:4]
    return render(request, 'home/index.html', {'packages': packages})

def packages(request):
    packages = Package.objects.all()
    return render(request, 'home/packages.html', {'packages': packages})