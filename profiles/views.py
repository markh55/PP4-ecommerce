from django.shortcuts import render

# Create your views here.
def profile_view(request):
    template = 'profiles/profile.html'
    context = {}
    return render(request, template, context)