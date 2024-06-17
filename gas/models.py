from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50,null=True)
    mobile = models.CharField(max_length=20,null=True)
    aadhar = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=30,null=True)

class Booking(models.Model):
    fullname = models.CharField(max_length=30,null=True)
    contact = models.CharField(max_length=30,null=True)
    booking_date = models.CharField(max_length=30,null=True)
    type = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=80,null=True)
    status = models.CharField(max_length=30,null=True)

class Feedback(models.Model):
    name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    contact = models.CharField(max_length=20,null=True)
    feedback = models.CharField(max_length=50,null=True)

