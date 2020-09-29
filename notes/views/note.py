from rest_framework import viewsets

from notes.models import Note
from notes.rest.serializers.note import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
