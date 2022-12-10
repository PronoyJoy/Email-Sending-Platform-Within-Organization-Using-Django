
from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)

    def __str__(self) -> str:
        return self.name

class Email(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    to = models.EmailField()
    frm = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sender')

    def __str__(self) -> str:
        return self.subject

