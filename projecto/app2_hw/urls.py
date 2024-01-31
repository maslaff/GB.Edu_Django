from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("users/", views.users, name="users"),
    path("products/", views.products, name="products"),
    path("user/<int:client_id>", views.orders_list, name="orders_list"),
    path(
        "user/<int:client_id>/prods/<str:period>",
        views.userorders_product_list,
        name="userorders_product_list_from",
    ),
    path(
        "user/<int:client_id>/prods/",
        views.userorders_product_list,
        name="userorders_product_list",
    ),
    path("product/<int:product_id>", views.product_form, name="product_edit"),
]
