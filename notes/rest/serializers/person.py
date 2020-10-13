from django.contrib.auth.models import User
from rest_framework import serializers

from notes.models.note import Note
from notes.models.person import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'phone', 'birthday',)


class UserSerializer(serializers.ModelSerializer):
    my_notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    read_notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    person = PersonSerializer(read_only=True, many=False)

    class Meta:
        model = User
        # depth = 1
        fields = ['id', 'url', 'person', 'first_name', 'last_name', 'username', 'my_notes', 'read_notes']
