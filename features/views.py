from django.shortcuts import render

def features(request):
    return render(request, 'features/features.html')

def about(request):
    return render(request, "features/about.html")

def faq(request):
    return render(request, "features/faq.html")

def portfolio(request):
    return render(request, "features/portfolio.html")