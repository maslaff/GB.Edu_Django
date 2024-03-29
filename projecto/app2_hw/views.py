from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
import logging
from datetime import date, datetime, timedelta

from app2_hw.models import Order, User, Product
from app2_hw.forms import ProductForm

log = logging.getLogger(__name__)


def about(request):
    log.info(f"About requested: {request}")
    return HttpResponse(
        """<H1>Hello Worldo!</H1>
                        <p><b>Hello All!</b></p>
                        <p><i>Hello, dear.</i></p>"""
    )


def index(request):
    log.info(f"Index requested: {request}")

    content = "<H1>Order List</H1><br><br>"

    orders = Order.objects.all()
    for order in orders:
        prod_list = "<br>".join(
            [f'- "{p.name}" : {p.price}' for p in order.products.all()]
        )
        content += f"Order date: {order.date_ordered.date()}<br>Customer: {order.customer}<br>Products:<br>{prod_list}<br>Total:\t{order.total_price}<br>"
        content += "<br>"

    return HttpResponse(content)


def orders_list(request, client_id):
    log.info(f"Orders list requested: {request}")

    cust = get_object_or_404(User, pk=client_id)

    orders = Order.objects.filter(customer=cust)
    context = {
        "user": cust,
        "orders": [
            {"order": order, "products": order.products.all()} for order in orders
        ],
    }

    return render(request, "app2_hw/orders.html", context)


def userorders_product_list(request, client_id, period=None):
    log.info(f"userorders_product_list requested: {request}")

    cust = get_object_or_404(User, pk=client_id)
    if period:
        periods = {"week": 7, "month": 30, "year": 365}
        if period not in periods:
            return HttpResponseNotFound("Not this period. Only year, month or week")
        from_date = datetime.today() - timedelta(days=periods[period])
        orders = Order.objects.filter(customer=cust, date_ordered__gt=from_date)
    else:
        orders = Order.objects.filter(customer=cust)

    prod_set = {prod for order in orders for prod in order.products.all()}

    context = {
        "user": cust,
        "products": prod_set,
    }

    return render(request, "app2_hw/uord_prods.html", context)


def users(request):
    log.info(f"Users requested: {request}")

    content = "<H1>User List</H1><br><br>"

    users = User.objects.all()
    for user in users:
        content += f"{user}<br>"

    return HttpResponse(content)


def products(request):
    log.info(f"products requested: {request}")

    content = "<H1>Product List</H1><br><br>"

    products = Product.objects.all()
    for product in products:
        content += f"{product.name} : {product.price} : {product.quantity} : {product.add_date}<br> {product.description}<br>"
        content += "<br>"

    return HttpResponse(content)


def product_form(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    message = "Продукт"
    if request.method == "POST":
        message = "Продукт изменен"
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            quantity = form.cleaned_data["quantity"]
            img = form.cleaned_data["img"]
            fs = FileSystemStorage()
            fs.save(img.name, img)
            product.image = img
            product.name = name
            product.description = description
            product.price = price
            product.quantity = quantity
            product.save()
    else:
        form = ProductForm(
            initial={
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity,
                "image_name": product.image,
            }
        )
        message = "Редактирование продукта"
    return render(
        request,
        "app2_hw/product_edit.html",
        {
            "form": form,
            "message": message,
            "prod_img": product.image,
        },
    )
