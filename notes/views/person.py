from django.contrib.auth.models import User
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from notes.rest.serializers.person import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Получаем базовый queryset и добавляем annotate."""
        queryset = super(UserViewSet, self).get_queryset()
        queryset = queryset.annotate(
            count_notes=Count('my_notes', distinct=True),
            count_read_notes=Count('read_notes', distinct=True)
        )
        return queryset
