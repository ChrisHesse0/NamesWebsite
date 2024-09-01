from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'landing/about.html')

def privacy(request):
    return render(request, 'landing/privacy.html')

def terms(request):
    return render(request, 'landing/terms.html')

def contact(request):
    return render(request, 'landing/contact.html')

def disclaimer(request):
    return render(request, 'landing/disclaimer.html')