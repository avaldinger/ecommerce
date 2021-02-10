from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    pass

class Bid(models.Model):
    startingBid = models.FloatField
    currentBid = models.FloatField
    bidTime = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    comment =  models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)


class AuctionListing(models.Model):
    NotDefined = "NotDefined"
    CATEGORIES = (
        (NotDefined, "Not defined"),
        ("Fashion", "Fashion"), 
        ("Toys", "Toys"),
        ("Electronics", "Electronics"),
        ("Home", "Home"),
        ("Car", "Car"),
        ("Travel", "Travel"),
        ("Fun", "Fun"),
    )
    item = models.CharField(max_length=125)
    description = models.CharField(blank=True, max_length=300)
    category = models.CharField(max_length=25, choices=CATEGORIES)
    sold = models.BooleanField()
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    image = models.CharField(blank=True, max_length=250)
    itemAdded = models.DateTimeField(auto_now_add=True)
    # bid = models.ForeignKey(Bid, blank=True, on_delete=models.CASCADE)  
    # comments = models.ForeignKey(Comment, blank=True, on_delete=models.CASCADE)


