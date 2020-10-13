from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from notes.models.person import Person
from notes.rest.serializers.person import PersonSerializer, UserSerializer


# class PersonViewSet(viewsets.ModelViewSet):
#     serializer_class = PersonSerializer
#     queryset = Person.objects.all()
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
