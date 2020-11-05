from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_fsm import FSMField, transition


class Note(models.Model):
    """Базовая модель заметки."""

    PRIORITY_CHOICE = (
        (1, _('Low')),
        (2, _('Middle')),
        (3, _('Above the average')),
        (4, _('High')),
        (5, _('Highest'))
    )

    TRANSITIONS = {
        'draft': _('Draft'),
        'published': _('Published'),
        'in_work': _('In work'),
        'done': _('Done')
    }

    state = FSMField(
        default='draft',
        protected=True,
        verbose_name=_('State')
    )

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_('Name')
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_notes',
        verbose_name=_('Owner')
    )

    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICE,
        blank=False,
        null=False,
        verbose_name=_('Priority')
    )

    readers = models.ManyToManyField(
        User,
        related_name='read_notes',
        blank=True,
        verbose_name=_('Readers')
    )

    is_done = models.BooleanField(
        default=False,
        verbose_name=_('Is done')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at')
    )

    solved_at = models.DateTimeField(
        auto_now=False,
        blank=True,
        null=True,
        db_index=True,
        verbose_name=_('Solved at')
    )

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

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

    def state_name(self):
        """Возвращает состояние заметки."""
        return self.TRANSITIONS.get(self.state)
    state_name.short_description = _('State')

    @transition(field=state, source='draft', target='published',
                custom=dict(admin=True, button_name=_('Draft to published')))
    def draft_to_published(self):
        """
        Из черновика в опубликовано.
        """
        pass

    @transition(field=state, source='published', target='draft',
                custom=dict(admin=True, button_name=_('Published to draft')))
    def published_to_draft(self):
        """
        Обратный статус. Из опубликовано в черновик.
        """
        pass

    @transition(field=state, source='published', target='in_work',
                custom=dict(admin=True, button_name=_('Published to in work')))
    def published_to_in_work(self):
        """
        Из опубликовано в работу.
        """
        pass

    @transition(field=state, source='in_work', target='published',
                custom=dict(admin=True, button_name=_('In work to Published')))
    def in_work_to_published(self):
        """
        Обратный статус. Из работы в опубликовано.
        """
        pass

    @transition(field=state, source='in_work', target='done',
                custom=dict(admin=True, button_name=_('In work to done')))
    def in_work_to_done(self):
        """
        Из работы в выполнено.
        """
        self.is_done = True
        self.solved_at = timezone.now()
        self.save()

    @transition(field=state, source='done', target='in_work',
                custom=dict(admin=True, button_name=_('Done to in work')))
    def done_to_in_work_(self):
        """
        Обратный статус. Из выполнено в работе.
        """
        self.is_done = False
        self.solved_at = None
        self.save()
