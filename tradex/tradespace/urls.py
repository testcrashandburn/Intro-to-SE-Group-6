from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("update_item/", views.updateItem, name="update_item"),
    path("process_order/", views.processOrder, name="process_order"),
    path("signup/", include("django.contrib.auth.urls")),
    path("tradespace/", views.tradespace, name="tradespace"),
    path("history/", views.history, name="history"),
    path("product_list/", views.product_list, name="product_list"),
    path("order_history/", views.order_history, name="order_history"),
    path(
        "remove_order/<int:order_id>/", views.remove_order, name="remove_order"
    ),
    path("compare/", views.compare, name="compare"),
    path("sellerhome/", views.sellerhome, name="sellerhome"),
    path(
        "remove_product/<str:product_name>",
        views.remove_product,
        name="remove_product",
    ),
    path("add_product/", views.add_product_page, name="add_product_page"),
]
