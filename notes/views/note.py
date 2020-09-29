from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from notes.models import Note
from notes.rest.serializers.note import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
