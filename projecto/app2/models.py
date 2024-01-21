from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=60)

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, age: {self.age}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")


class Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
