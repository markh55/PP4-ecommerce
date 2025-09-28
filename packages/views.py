from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Package, Review, Rating

def package_list(request, tier=None):
    packages = Package.objects.all()
    if tier:
        packages = packages.filter(tier=tier)
    return render(request, 'packages/package_list.html', {'packages': packages, 'tier': tier})

def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug)
    return render(request, 'packages/package_detail.html', {'package': package})

@login_required
def add_review(request, slug):
    package = get_object_or_404(Package, slug=slug)

    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        title = request.POST.get('title')
        body = request.POST.get('body')

        rating, created = Rating.objects.get_or_create(
            package=package,
            user=request.user,
            defaults={'rating': rating_value}
        )
        if not created:
            rating.rating = rating_value
            rating.save()

        Review.objects.create(
            package=package,
            user=request.user,
            title=title,
            body=body
        )

        messages.success(request, 'Your review has been added!')
        return redirect('packages:package_detail', slug=slug)