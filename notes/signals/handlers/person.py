from django.db.models.signals import post_delete
from django.dispatch import receiver

from notes.models.person import Person


@receiver(post_delete, sender=Person, dispatch_uid='invalidate_person_and_delete')
def invalidate_person_and_delete(sender, instance, **kwargs):
    """Сигнал удаляющий пользователя при удалении персоны."""
    user = instance.user
    if user and not (user.is_staff or user.is_superuser):
        user.delete()
