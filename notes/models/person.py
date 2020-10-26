from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    """Расширенная модель User с дополнительными полями."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='person',
        null=True
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

    # todo: last_activity

    def __str__(self):
        return f'{self.user.username} id:{self.id}'

    @property
    def username(self):
        return self.user.username

    @username.setter
    def username(self, value):
        self.user.username = value

    @property
    def first_name(self):
        return self.user.first_name

    @first_name.setter
    def first_name(self, value):
        self.user.first_name = value

    @property
    def last_name(self):
        return self.user.last_name

    @last_name.setter
    def last_name(self, value):
        self.user.last_name = value

    @property
    def email(self):
        return self.user.email

    @email.setter
    def email(self, value):
        self.user.email = value

    @property
    def get_person(self):
        return self.user
