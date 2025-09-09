from django.shortcuts import get_object_or_404, render
from .models import Package

# Create your views here.
def package_list(request, tier=None):
    packages = Package.objects.all()
    if tier:
        packages = packages.filter(tier=tier)
    return render(request, 'packages/package_list.html', {'packages': packages, 'tier': tier})

def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    return render(request, 'packages/package_detail.html', {'package': package})

