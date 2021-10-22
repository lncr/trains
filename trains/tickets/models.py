from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ticket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    trip = models.ForeignKey('trips.Trip', on_delete=models.PROTECT, related_name='tickets')
    price = models.DecimalField(decimal_places=2, max_digits=10)
