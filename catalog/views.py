from django.shortcuts import render, HttpResponse
from .models import Product, Contact

# Create your views here.

def home(request):
    products = Product.objects.order_by('-created_at')[0:5]
    for product in products:
        print(product)

    return render(request, 'catalog/home.html')

def contacts(request):
    contact = Contact.objects.first()

    context = {
        'contact': contact
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html', context)

