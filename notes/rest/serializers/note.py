from rest_framework import serializers

from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    count_readers = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ('id', 'name', 'owner', 'priority', 'readers', 'count_readers', 'url', 'is_done', 'created_at')

    def get_count_readers(self, instance):
        return instance.readers.all().count()
