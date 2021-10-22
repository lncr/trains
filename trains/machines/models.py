from django.db import models


class Machine(models.Model):
    max_capacity = models.IntegerField()
