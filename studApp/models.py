from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StdModel(models.Model):

    # FEE_CHOICES=(('paid','paid'),('pending','pending'))
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100 )
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()

