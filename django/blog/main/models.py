from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.


class Reader(models.Model):
    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='reader',
    )

    registration_date = models.DateTimeField(default=datetime.now, blank=True)

