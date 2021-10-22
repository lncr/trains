from django.db import models


class Machine(models.Model):
    """
    Model for representing train machines.
    """
    max_capacity = models.IntegerField(help_text='Maximum amount of passengers machine can carry')
