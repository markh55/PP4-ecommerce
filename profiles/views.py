from django.shortcuts import render

# Create your views here.
def profile(request):
    template = 'profiles/profile.html'
    context = {}
    return render(request, template, context)