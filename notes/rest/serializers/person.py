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
    # person = PersonSerializer(read_only=True, many=False)
    phone = serializers.CharField(source='person.phone', read_only=True)
    birthday = serializers.ReadOnlyField(source='person.birthday', read_only=True)
    person_id = serializers.ReadOnlyField(source='person.id', read_only=True)

    class Meta:
        model = User
        # depth = 1
        fields = ('id', 'url', 'first_name', 'last_name', 'username', 'email',
                  'person_id', 'phone', 'birthday', 'my_notes', 'read_notes')

