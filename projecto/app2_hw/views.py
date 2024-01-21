from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import date

from app2_hw.models import Order, User, Product

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

        # .join([str(order) for order in orders])

    return HttpResponse(content)


def users(request):
    log.info(f"Users requested: {request}")

    content = "<H1>User List</H1><br><br>"

    users = User.objects.all()
    for user in users:
        content += f"{user}<br>"

        # .join([str(order) for order in users])

    return HttpResponse(content)


def products(request):
    log.info(f"products requested: {request}")

    content = "<H1>Product List</H1><br><br>"

    products = Product.objects.all()
    for product in products:
        content += f"{product.name} : {product.price} : {product.quantity} : {product.add_date}<br> {product.description}<br>"
        content += "<br>"
        # .join([str(order) for order in products])

    return HttpResponse(content)
