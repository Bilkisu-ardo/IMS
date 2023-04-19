from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html')

def customers(request):
    return render(request, 'customers.html')
# Create your views here.
