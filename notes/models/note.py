from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    PRIORITY_CHOICE = (
        (1, 'Низкий'),
        (2, 'Средний'),
        (3, 'Выше среднего'),
        (4, 'Высокий'),
        (5, 'Наивысший')
    )

    name = models.CharField(max_length=255, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_notes')
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICE, blank=False, null=False)
    readers = models.ManyToManyField(User, related_name='read_notes', blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    solved_at = models.DateTimeField(auto_now=False, blank=True, null=True, db_index=True)

    def __str__(self):
        return f'Name: {self.name}, owner: {self.owner}'
