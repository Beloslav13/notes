from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Note(models.Model):
    """Базовая модель заметки."""

    PRIORITY_CHOICE = (
        (1, 'Низкий'),
        (2, 'Средний'),
        (3, 'Выше среднего'),
        (4, 'Высокий'),
        (5, 'Наивысший')
    )

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_notes'
    )

    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICE,
        blank=False,
        null=False
    )

    readers = models.ManyToManyField(
        User,
        related_name='read_notes',
        blank=True
    )

    is_done = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    solved_at = models.DateTimeField(
        auto_now=False,
        blank=True,
        null=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def get_detail_url(self):
        return reverse('note_detail', args=[self.pk])

    def __str__(self):
        return f'id note: {self.id}, owner: {self.owner}'

    @property
    def owner_username(self):
        """Получить username владельца заметки."""
        return self.owner.username

    @property
    def owner_first_name(self):
        """Получить first_name владельца заметки."""
        return self.owner.first_name

    @property
    def owner_last_name(self):
        """Получить last_name владельца заметки."""
        return self.owner.last_name

    @property
    def owner_person(self):
        """Получить персону владельца заметки."""
        return self.owner.person
