import pytest    
from product.models import Product   
from accounts.models import CustomUser

@pytest.mark.django_db 
def test_product():    
     
    print(Product.objects.all())
    testuser=CustomUser.objects.create(user_type="buyer")

    testproduct = Product.objects.create( _productID = 3,
    _productName = "pytest",
    _productDescript = "test description",
    price = "0.04",
    quantity = "2",
    seller = testuser)

    assert testproduct._productID==3      
