from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from django_fsm.signals import post_transition

from notes.models.note import Note


# Test
@receiver(post_save, sender=Note, dispatch_uid='invalidate_note')
def invalidate_note(sender, instance, **kwargs):
    pass


@receiver(post_transition, sender=Note, dispatch_uid='invalidate_note_transition')
def invalidate_note_transition(sender, instance, name, source, target, **kwargs):
    if name:
        instance.owner.person.last_activity = timezone.now()
        instance.owner.person.save()
