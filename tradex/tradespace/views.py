from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
import json
from .models import OrderItem, Order, Product, ShippingAddress
import datetime
from .forms import ProductForm


def tradespace(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False
        )
        cartItems = order.get_cart_items
    else:
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    if request.user == "AnonymousUser":
        return render(request, "tradespace/tradespace.html", context)
    else:
        if request.user.user_type == "seller":
            return redirect("sellerhome")
        else:
            return render(request, "tradespace/tradespace.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False
        )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
        cartItems = order["get_cart_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "tradespace/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False
        )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
        cartItems = order["get_cart_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "tradespace/checkout.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print("Action:", action)
    print("Product:", productId)
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False
    )
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product
    )
    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Item was added", safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False
        )
        total = float(data["form"]["total"])
        print(transaction_id)
        order.transaction_id = transaction_id
        if total == order.get_cart_total:
            order.complete = True
            order.save()
        if order.shipping is True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data["shipping"]["address"],
                city=data["shipping"]["city"],
                state=data["shipping"]["state"],
                zipcode=data["shipping"]["zipcode"],
            )
    else:
        print("User is not logged in")

    return JsonResponse("Payment submitted..", safe=False)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "tradespace/signup.html"


def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False
        )
        cartItems = order.get_cart_items
    else:
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    return render(request, "tradespace/home.html", context)


def history(request):
    if request.user.is_authenticated:
        historylist = [
            Order.objects.values_list(),
            Order.customer.field.get_attname(),
        ]
    else:
        historylist = {
            "get_cart_total": 0,
            "get_cart_items": 0,
            "shipping": False,
        }
    context = {"historylist": historylist}
    return render(request, "tradespace/history.html", context)


def product_list(request):
    products = Product.objects.all()
    query = request.GET.get("q")
    if query:
        products = products.filter(name__icontains=query)

    return render(
        request, "tradespace/product_list.html", {"products": products}
    )


def order_history(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(customer=request.user)
        return render(
            request, "tradespace/order_history.html", {"orders": orders}
        )
    else:
        return redirect("login")


def compare(request):
    query1 = request.GET.get("q1")
    query2 = request.GET.get("q2")
    product1 = None
    product2 = None
    if query1:
        product1 = Product.objects.filter(name__icontains=query1).first()
    if query2:
        product2 = Product.objects.filter(name__icontains=query2).first()
    return render(
        request,
        "tradespace/compare.html",
        {"product1": product1, "product2": product2},
    )


def sellerhome(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(creator=request.user)
        return render(
            request, "tradespace/sellerhome.html", {"products": products}
        )
    else:
        return redirect("login")


def remove_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.is_authenticated and order.customer == request.user:
        order.delete()
    return redirect("order_history")


def remove_product(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    if request.user.is_authenticated and product.creator == request.user:
        product.delete()
    return redirect("sellerhome")


def add_product_page(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            return redirect("sellerhome")
    else:
        form = ProductForm()
    return render(request, "tradespace/add_product_page.html", {"form": form})
