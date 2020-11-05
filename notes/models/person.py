from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    """Расширенная модель User с дополнительными полями."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='person',
        null=True,
        verbose_name=_('User')
    )

    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=None,
        verbose_name=_('Phone')
    )

    birthday = models.DateField(
        null=True,
        blank=True,
        default=None,
        verbose_name=_('Birthday')
    )

    last_activity = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Last activity')
    )

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

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
    def full_name(self):
        """
        Внимание! Метод вернёт либо полное имя, либо email если он есть либо в крайнем случае username!
        """
        full_name = f'{self.user.first_name} {self.user.last_name}'
        return full_name if len(full_name) > 1 else self.user.email or self.user.username

    @property
    def email(self):
        return self.user.email

    @email.setter
    def email(self, value):
        self.user.email = value

    @property
    def get_person(self):
        return self.user
