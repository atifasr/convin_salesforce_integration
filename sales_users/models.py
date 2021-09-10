from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.fields import CharField

# Create your models here.


class UserData(models.Model):
    user_id = models.CharField(max_length=255,null=True)
    username = models.CharField(max_length=30,blank=True,null=True)
    lastname = models.CharField(max_length=30,blank=True,null=True)
    firstname = models.CharField(max_length=30,blank=True,null=True)
    company_name= models.CharField(max_length=30,blank=True,null=True)
    city = models.CharField(max_length=20,null=True)
    timezonesidekey = models.CharField(max_length=20,null=True)
    aboutme = models.TextField(blank=True,default='good',null=True)
    email = models.EmailField(null=True)
    isactive = models.BooleanField(default=False)

    def __str__(self):
        return self.lastname



class AccountData(models.Model):
    account_id = models.CharField(max_length=255,null=True)
    name = models.CharField(max_length=30,null=True)
    photourl = models.URLField(null=True)
    billingaddress = models.CharField(max_length=30,null=True)
    account_number = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name


class ContactData(models.Model):
    contact_id = models.CharField(max_length=255,null=True)
    accountid = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    firstname = models.CharField(max_length=40,null=True)
    name= models.CharField(max_length=34,null=True)
    mailingstreet = models.CharField(max_length=30,null=True)
    phone_no = models.CharField(max_length=30,null=True)
    birth_day = models.DateTimeField(null=True)
    lead_source = models.CharField(max_length=40,null=True)
    email = models.EmailField(null=True)
    department = models.CharField(max_length=30,null=True)
    photourl = models.URLField(null=True)

    def __str__(self):
        if self.name == None:
            return ' '
        else:
            return self.firstname