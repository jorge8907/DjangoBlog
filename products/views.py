from django.shortcuts import render
from .models import Product
from .models import Category
#1Busqueda
from django.db.models import Q
#1Busqueda

# Create your views here.
def home(request):
    #1Busqueda
    
    queryset = request.GET.get("buscar")
    #1Busqueda
   
    products = Product.objects.all()
    #products = Product.objects.filter(
    #    Q(categories=1)| 
     #   Q(categories=2)
     #   ).distinct()
    
    #2Busqueda
    if queryset:
        products = Product.objects.filter(
           Q(name__icontains = queryset) | 
            Q(price__icontains = queryset)     
        ).distinct()
            
        
    #2Busqueda
    #print(request.user.cart.products.all())
    
    #products = Category.objects.get(pk=1).products.all()
    print(products)
    return render(request, "pages/home.html", {
        "products":products
    })
