import pytest
from .models import Product, CustomUser, OrderItem,Order, ShippingAddress
from django.test import RequestFactory
from django.http import HttpResponse
from django.utils import timezone


@pytest.mark.django_db
def test_user_db():
    print(Product.objects.all())
    testuser = CustomUser.objects.create(user_type="buyer")

    assert testuser.user_type == "buyer"


@pytest.mark.django_db
def test_product_db():
    print(Product.objects.all())
    testuser = CustomUser.objects.create(user_type="buyer")
    testproduct = Product.objects.create(
        name="pytest", digital=True, price="0.04", image="", creator=testuser
    )
    assert testproduct.name == "pytest"


@pytest.mark.django_db
def test_order_db():
    testuser = CustomUser.objects.create(user_type="buyer")
    testOrder = Order.objects.create(
        customer=testuser,
        date_ordered=timezone.now(),
        # transactionTime = datetime.datetime(2015, 10, 11, 23, 55, 59, 342380)
        transaction_id=1,
        complete=True,
    )
    assert testOrder.transaction_id == 1


@pytest.mark.django_db
def test_address_db():
    testuser = CustomUser.objects.create(user_type="buyer")
    testOrder = Order.objects.create(
        customer=testuser,
        date_ordered=timezone.now(),
        # transactionTime = datetime.datetime(2015, 10, 11, 23, 55, 59, 342380)
        transaction_id=1,
        complete=True,
    )
    testaddress = ShippingAddress.objects.create(
        customer=testuser,
        order=testOrder,
        address="123 test rd",
        city="",
        state="",
        zipcode="",
        date_added="",
    )
    assert testaddress.address == "123 test rd"

@pytest.mark.django_db
def test_Order_Item():
    testuser = CustomUser.objects.create(user_type="buyer")
    testOrder = Order.objects.create(
        customer=testuser,
        date_ordered=timezone.now(),
        # transactionTime = datetime.datetime(2015, 10, 11, 23, 55, 59, 342380)
        transaction_id=1,
        complete=True,
    )
    testproduct = Product.objects.create(
        name="pytest", digital=True, price="0.04", image="", creator=testuser
    )
    testOrderItem = OrderItem.objects.create(
    product = testproduct,
    order = testOrder,
    quantity = 9,
    date_added = timezone.now(),
    )


@pytest.mark.django_db
def test_transaction_db():
    testuser = CustomUser.objects.create(user_type="buyer")
    timezone.now()
    # d = datetime.datetime(2015, 10, 11, 23, 55, 59, 342380)
    testtransaction = Order.objects.create(
        customer=testuser,
        date_ordered=timezone.now(),
        # transactionTime = datetime.datetime(2015, 10, 11, 23, 55, 59, 342380)
        transaction_id=1,
        complete=True,
    )
    assert testtransaction.transaction_id == 1


@pytest.mark.django_db
def test_product_url():
    path = "/product"
    request = RequestFactory().get(path)
    response = HttpResponse(request)
    assert response.status_code == 200


def test_admin_url():
    path = "/admin"
    request = RequestFactory().get(path)
    response = HttpResponse(request)
    assert response.status_code == 200


def test_signup_url():
    path = "/accounts/signup"
    request = RequestFactory().get(path)
    response = HttpResponse(request)
    assert response.status_code == 200


def test_login_url():
    path = "/accounts/login/"
    request = RequestFactory().get(path)
    response = HttpResponse(request)
    assert response.status_code == 200


#   response = admin_client.get('/admin/')
#  assert response.status_code == 200


# path("", views.index, name = "index")
# def index(request):
#   return HttpResponse(Product.objects.all())
# path("", TemplateView.as_view(template_name="home.html"), name="home"),
# path("admin/", admin.site.urls),
# path("accounts/", include("accounts.urls")),
