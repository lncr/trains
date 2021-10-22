from django.db import models


class Trip(models.Model):
    """
    Model for representing a trip of train from beginning to end
    """
    stations = models.ManyToManyField('directory.Station', through='TripStation')
    train = models.ForeignKey('machines.Machine', on_delete=models.PROTECT, related_name='trips')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class TripStation(models.Model):
    """
    Link model for stations-trips relation. Represents stops of the train
    """
    station = models.ForeignKey('directory.Station', on_delete=models.CASCADE, related_name='trip_station_links')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_station_links')
    arrival_time = models.DateTimeField()
    queue = models.PositiveIntegerField()
