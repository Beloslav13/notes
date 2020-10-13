# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# from notes.models.person import Person
#
#
# @receiver(post_save, sender=User, dispatch_uid='invalidate_note')
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Person.objects.create(person=instance)
#     instance.person.save()
