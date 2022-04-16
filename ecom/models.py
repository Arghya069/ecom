import os
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):

    """
    Custom User Manager for the user class.
    methods : 
    create_superuser :- used by the manage.py createsuperuser command
    create_user :- the default user creation method is_admin=false,is_staff=false,is_active=true
    ,additional arguments can be passed
    """
    def create_superuser(self,mobile,Email,first_name,password,**other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(mobile,Email,first_name,password,**other_fields)


    def create_user(self,mobile,Email,first_name,password,**other_fields):
        if not mobile:
            raise ValueError(("You must provide an employee Id"))

        user = self.model(mobile=mobile,Email=Email,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user 

class User(AbstractBaseUser,PermissionsMixin):

    mobile = models.CharField(max_length=12,unique=True,primary_key=True)
    Email = models.EmailField(max_length=100,unique=True,blank=False)
    first_name = models.CharField(max_length=150,blank=False)
    last_name = models.CharField(max_length=150,blank=True)
    photo   = models.ImageField(upload_to='profile_pics',default='profile_pics/default.png')
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['Email','first_name','password']

    def __str__(self):
        return self.mobile


class product(models.Model):
    product_id=models.AutoField
    productname=models.CharField(max_length=100,primary_key=True)
    productdesc=models.CharField(max_length=300)
    product_cost=models.FloatField(null=False)
    Date_added=models.DateTimeField
    available_quantity=models.IntegerField(default=1)
    product_image=models.ImageField(upload_to='media',default='default.png')