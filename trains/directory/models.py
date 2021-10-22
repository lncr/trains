from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)


class Station(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='stations')
