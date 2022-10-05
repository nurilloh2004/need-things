from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=64, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)


    def __str__(self) -> str:
        return self.full_name

    def save(self, *args, **kwargs):
        password = self.password
        self.set_password(password)
        print("sending sms to email")
        send_mail(
            "Created user",
            "Test message",
            EMAIL_HOST_USER,
            ["keen.oncoding04@gmail.com"],
            fail_silently=False
        )
        return super(User,self).save(*args, **kwargs)

    
class TypeProduct(models.Model):
    name = models.CharField(max_length=64) 


    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=64)
    amount = models.IntegerField()
    describtion = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    price_for_day = models.IntegerField()
    VAT = models.CharField(max_length=64)
    unit_of_measure = models.CharField(max_length=64)
    sign_image = models.ImageField()
    created_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    





class Service(models.Model):
    name = models.CharField(max_length=64)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name





class Form(models.Model):
    full_name = models.CharField(max_length=64)
    phone_number = models.IntegerField()


    def __str__(self) -> str:
        return self.full_name