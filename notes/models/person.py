from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):

    person = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None
    )

    birthday = models.DateField(
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return f'{self.person.username}'
