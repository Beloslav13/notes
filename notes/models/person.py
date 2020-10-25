from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):

    person = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user'
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
        return f'{self.person.username} id:{self.id}'

    @property
    def username(self):
        return self.person.username

    @username.setter
    def username(self, value):
        self.person.username = value

    @property
    def first_name(self):
        return self.person.first_name

    @first_name.setter
    def first_name(self, value):
        self.person.first_name = value

    @property
    def last_name(self):
        return self.person.last_name

    @last_name.setter
    def last_name(self, value):
        self.person.last_name = value

    @property
    def email(self):
        return self.person.email

    @email.setter
    def email(self, value):
        self.person.email = value

    @property
    def get_person(self):
        return self.person
