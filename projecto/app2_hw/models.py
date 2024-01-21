from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Registration: {self.reg_date}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # prod_list = "\n".join(
        #     [f"\t{Product.objects.filter(id = prod).name}" for prod in self.products]
        # )
        prod_list = "\n".join([f'- "{p.name}" {p.price}' for p in self.products.all()])
        return f"Order date: {self.date_ordered}\nCustomer: {self.customer}\nProducts:\n{prod_list}\nTotal:\t{self.total_price}\n"
