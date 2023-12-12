from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    map_url = models.URLField()
    img_url = models.URLField()
    location = models.CharField(max_length=200)
    has_sockets = models.BooleanField()
    has_toilet = models.BooleanField()
    has_wifi = models.BooleanField()
    can_take_calls = models.BooleanField()
    seats = models.IntegerField()
    coffee_price = models.FloatField()
