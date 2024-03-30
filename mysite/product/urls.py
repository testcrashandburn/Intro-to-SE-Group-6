from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index")
    #path("product/", ProductView.as_view(template_name="product.html"), name = "product")
# path("product/", TemplateView.as_view(template_name="product.html"), name="product"),
]