from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
GENDER_CHOICES = [    ('M', 'Male'),    ('F', 'Female'),    ('O', 'Other'),]
MEAL_CHOICE=[    ('B', 'Breakfast'),    ('L', 'Lunch'),    ('D', 'Dinner'),]
PMT_CHOICE=[('C','Card'), ('U','UPI')]
class Admin(models.Model):
    admin_id=models.IntegerField(primary_key=True)  
    admin_name=models.CharField(max_length=10)
    admin_lname=models.CharField(max_length=10)
    admin_pswd=models.CharField(max_length=8)
    admin_gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    admin_email=models.EmailField(null=True)
    admin_dob=models.DateField(null=True)
    
    

class Customers(models.Model):
        customer_id=models.IntegerField()
        customer_fname=models.CharField(max_length=10)    
        customer_lname=models.CharField(max_length=10)
        customer_gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
        customer_cno=models.CharField(max_length=20)
        customer_email=models.EmailField(unique=True)
        customer_dob=models.DateField(null=True)
        customer_pswd=models.CharField(max_length=8)
     
       
class Agent(models.Model):
        agent_id=models.IntegerField()
        agency_name=models.CharField(max_length=10)    
        agent_fname=models.CharField(max_length=10)    
        agent_lname=models.CharField(max_length=10)
        agent_gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
        agent_cno=models.IntegerField()
        agent_email=models.EmailField(unique=True)
        agent_dob=models.DateField()
        agent_pswd=models.CharField(max_length=8)
        #agent_pic=models.ImageField()

class Address(models.Model):
    add_id=models.IntegerField()
    add_no=models.IntegerField()
    add_street=models.CharField(max_length=10)
    add_city=models.CharField(max_length=10)
    add_state=models.CharField(max_length=10)
    add_country=models.CharField(max_length=10)
    add_zip=models.IntegerField()


class Places(models.Model):
    place_id=models.IntegerField()
    place_name=models.CharField(max_length=10)
 #  place_pic=models.ImageField()
    place_type=models.CharField(max_length=10)

class Packages(models.Model):
    pkg_id=models.IntegerField()
    pkg_type=models.CharField(max_length=10)
    pkg_title=models.CharField(max_length=10)
    dep_date=models.DateField()
    pkg_from=models.CharField(max_length=10)
    pkg_to=models.CharField(max_length=10)
   # pkg_pic=models.ImageField()
    pkg_dec=models.CharField(max_length=100)
    pkg_price=models.IntegerField()
    pkg_days=models.IntegerField()
    pkg_night=models.IntegerField()
    tota_seats=models.IntegerField()
    avil_seats=models.IntegerField()
    pkg_status=models.BooleanField(default=True)

class Itinerary(models.Model):
    itr_id=models.IntegerField()
    vcl_type=models.CharField(max_length=10)

class Day(models.Model):
    day_id=models.IntegerField()
    day_title=models.CharField(max_length=10)
    day_no=models.IntegerField()
    day_place=models.CharField(max_length=10)
    hotspot=models.CharField(max_length=10)
    day_desc=models.CharField(max_length=10)

class Hotel(models.Model):
    hotel_id=models.IntegerField()
    hotel_name=models.CharField(max_length=20)
    hotel_type=models.CharField(max_length=20)
    meal_type=models.CharField(max_length=10,choices=MEAL_CHOICE)

class Booking(models.Model):
    bkg_id=models.IntegerField()
    bkg_date=models.DateField()
    
class Payment(models.Model):
    payment_id=models.IntegerField()
    payment_time=models.TimeField()
    payment_method=models.CharField(max_length=10,choices=PMT_CHOICE)
    payment_amt=models.IntegerField()

class Cancellation(models.Model):
    cl_id=models.IntegerField()
    cl_time=models.TimeField()
    cl_reason=models.CharField(max_length=255)
    refund_st=models.BooleanField(default=False)

class Enquiry(models.Model):
    eqry_id=models.IntegerField()
    eqry_name=models.CharField(max_length=20)
    eqry_email=models.EmailField(unique=True)
    eqry_remark=models.CharField(max_length=100)
    eqry_type=models.CharField(max_length=10)
    eqry_date=models.DateField()

class Feedback(models.Model):
    fb_id=models.IntegerField()
    fb=models.CharField(max_length=255)
    
    
# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)

#     avatar = models.ImageField(null=True, default="avatar.png")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []"""