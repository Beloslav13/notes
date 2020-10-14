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
    phone = serializers.CharField(source='person.phone', allow_blank=True, allow_null=True)
    birthday = serializers.CharField(source='person.birthday', allow_blank=True, allow_null=True)
    person_id = serializers.IntegerField(source='person.id', read_only=True)
    person = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        # depth = 1
        fields = ('id', 'url', 'person', 'first_name', 'last_name', 'username', 'email',
                  'person_id', 'phone', 'birthday', 'my_notes', 'read_notes')

    def create(self, validated_data):
        # При создании кастомного юзера, создаём расширенного.
        persons_data = validated_data.pop('person')
        validated_data.pop('my_notes')
        validated_data.pop('read_notes')
        user = User.objects.create(**validated_data)
        Person.objects.create(person=user, **persons_data)
        return user
