from django.core.management.base import BaseCommand, CommandError

from notes.models.person import Person
from django.contrib.auth.models import User


class Command(BaseCommand):

    # todo: Возможно пригодится
    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         '--amount_days',
    #         dest='amount_days',
    #         type=int,
    #         default=365
    #     )

    def handle(self, *args, **options):
        # Получили айдишники всех пользоваетелй у которых есть персоны.
        user_ids = Person.objects.all().values_list('user_id', flat=True)
        # Получили айдишники всех пользователей у которых нет персон, благодаря тому,
        # что исключили те айдшинки у которых есть персоны.
        User.objects. \
            filter(is_superuser=False, is_staff=False). \
            exclude(id__in=user_ids).delete()
