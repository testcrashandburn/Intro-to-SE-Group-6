import pytest    
from product.models import Product   
from accounts.models import CustomUser
from transaction.models import Transaction
from django.urls import reverse
from django.test import RequestFactory
from product.views import index
from django.http import HttpResponse
import datetime
from django.utils import timezone
#import pytz
from django.test import Client

@pytest.mark.django_db 
def test_user_db():    
     
    print(Product.objects.all())
    testuser=CustomUser.objects.create(user_type="buyer")

    assert testuser.user_type=="buyer"

@pytest.mark.django_db 
def test_product_db():    
     
    print(Product.objects.all())
    testuser=CustomUser.objects.create(user_type="buyer")
    testproduct = Product.objects.create( _productID = 3,
        _productName = "pytest",
        _productDescript = "test description",
        price = "0.04",
        quantity = "2",
        seller = testuser
    )
    assert testproduct._productID==3    

@pytest.mark.django_db 
def test_transaction_db():    
     
   # print(Product.objects.all())
    testuser=CustomUser.objects.create(user_type="buyer")

    
    testproduct = Product.objects.create( _productID = 3,
        _productName = "pytest",
        _productDescript = "test description",
        price = "0.04",
        quantity = "2",
        seller = testuser
    )
    timezone.now()
    #d = datetime.datetime(2015, 10, 11, 23, 55, 59, 342380)
    testproduct = Transaction.objects.create( transactionID = 1,
        productInfo = testproduct,
        sellerInfo = testuser,
        #transactionTime = datetime.datetime(2015, 10, 11, 23, 55, 59, 342380)
        transactionTime = timezone.now()
    )




@pytest.mark.django_db
def test_index_url():
    path = "/"
    request = RequestFactory().get(path)
    response = index(request)
    assert response.status_code == 200
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
    path= "/accounts/login/"
    request = RequestFactory().get(path)
    response = HttpResponse(request)
    assert response.status_code == 200



 #   response = admin_client.get('/admin/')
  #  assert response.status_code == 200


#path("", views.index, name = "index")
#def index(request):
 #   return HttpResponse(Product.objects.all())
   # path("", TemplateView.as_view(template_name="home.html"), name="home"),
   # path("admin/", admin.site.urls),
    #path("accounts/", include("accounts.urls")),