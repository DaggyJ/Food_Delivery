from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CITY_CHOICES= (
    ('NBI','Nairobi'),
    ('KSM','Kisumu'),
    ('ELD','Edldoret'),
    ('Nak','Nakuru'),
    ('MBS','Mombasa')
)
CATEGORY_CHOICES=(
    ('FR','Fruits'),
    ('VG','Vegetables'),
    ('DY','Dairy'),
    ('GN','Grains'),
    ('PF','Protein foods')
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price  = models.IntegerField(null=True)
    discounted_price = models.IntegerField(null=True)
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    



class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(choices= CITY_CHOICES, max_length=100)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    
    def __str__(self):
        return self.name