from django.shortcuts import render


def index(request):
    return render(request, 'accounts/index.html', {})


def profile(request):
    return render(request, 'accounts/profile.html', {})
