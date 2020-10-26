from django.contrib.auth.models import User
from rest_framework import serializers

from notes.models.note import Note
from notes.models.person import Person

import logging

logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s %(message)s')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'phone', 'birthday',)


class UserSerializer(serializers.ModelSerializer):
    my_notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    read_notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    phone = serializers.CharField(source='person.phone', allow_blank=True, allow_null=True)
    birthday = serializers.CharField(source='person.birthday')
    person = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'person', 'first_name', 'last_name', 'username', 'email',
                  'phone', 'birthday', 'my_notes', 'read_notes')

    def validate(self, data):
        attr_errors = {}
        if not data['person']['birthday']:
            attr_errors['birthday'] = "Это поле не было заполнено."
            raise serializers.ValidationError(attr_errors)
        return data

    def create(self, validated_data):
        # При создании кастомного юзера, создаём персону.
        persons_data = validated_data.pop('person')
        validated_data.pop('my_notes')
        validated_data.pop('read_notes')
        user = User.objects.create(**validated_data)
        try:
            Person.objects.create(user=user, **persons_data)
        except TypeError as exc:
            person = Person.objects.create(user=user)
            logging.error(f'Произошла ошибка при создании персоны в сериалайзере: {exc}\n'
                          f'user id {user.id}, person id {person.id}')
        return user
