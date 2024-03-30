from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product
# Create your views here.


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy




#print(Product.objects.all())
def index(request):
    return HttpResponse(Product.objects.all())


#class ProductView(CreateView):
    #success_url = reverse_lazy("login")
  #  Product.objects.all()
   # template_name = "product.html"
    