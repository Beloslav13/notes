from django.db.models.signals import post_save
from django.dispatch import receiver

from notes.models.note import Note


# Test
@receiver(post_save, sender=Note, dispatch_uid='invalidate_note')
def invalidate_note(sender, instance, **kwargs):
    pass
