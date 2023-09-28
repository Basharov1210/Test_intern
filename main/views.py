from django.shortcuts import render
from django.views.generic import DetailView

from .models import AboutMe


def home(request):
    return render(request, 'main/home.html')


def about(request):
    about_me = AboutMe.objects.get(id=1)
    context = {
        'about_me': about_me
    }
    return render(request, 'main/about.html', context=context)
