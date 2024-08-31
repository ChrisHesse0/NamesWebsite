from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'landing/about.html')

def privacy(request):
    return render(request, 'landing/privacy.html')

