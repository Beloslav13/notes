from rest_framework import serializers

from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'name', 'owner', 'priority', 'readers',  'url', 'is_done', 'created_at')
