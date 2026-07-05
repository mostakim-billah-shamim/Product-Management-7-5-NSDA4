from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    user_type=[
        ('admin','admin'),
        ('customer','customer'),
    ]
    user_type=models.CharField(choices=user_type, max_length=30, null=True)

    def __str__(self):
        return self.username


class AdminModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30, null=True)
    description=models.TextField(null=True)
    address=models.CharField(max_length=30, null=True)
    phone=models.CharField(max_length=30, null=True)
    time=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.store_name}-{self.user.username}"


class CustomerModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=30, null=True)
    address=models.CharField(max_length=30, null=True)
    phone=models.CharField(max_length=30, null=True)
    time=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.full_name






class CategoryModel(models.Model):
    name=models.CharField(max_length=120, null=True, unique=True)
    description= models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name




class ProductModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


# Create your models here.
