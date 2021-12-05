from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.shortcuts import render, get_object_or_404, redirect, reverse

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code

class Movie(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image= models.ImageField(upload_to='MovieImages', default='default_movie.jpg')
    is_released = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    release_date = models.DateField()

    def __str__(self):
        return self.name