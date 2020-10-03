from django.utils import timezone
from rest_framework import serializers

from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    count_readers = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ('id', 'name', 'owner', 'priority', 'readers', 'count_readers', 'url', 'is_done', 'created_at', 'solved_at')

    def get_count_readers(self, instance):
        return instance.readers.all().count()

    def validate(self, data):
        # todo: validate
        return data

    @staticmethod
    def _update_entity(self, instance, validated_data):
        is_done = validated_data.pop('is_done', None)
        if is_done is not None:
            if not instance.is_done and is_done != instance.is_done:
                validated_data.pop('solved_at', None)
                instance.solved_at = timezone.now()
                instance.is_done = is_done
            elif instance.is_done and instance.solved_at and is_done != instance.is_done:
                validated_data.pop('solved_at', None)
                instance.solved_at = None
                instance.is_done = is_done
            instance.save()

    def update(self, instance, validated_data):
        self._update_entity(self, instance, validated_data)
        return super(self.__class__, self).update(instance, validated_data)

