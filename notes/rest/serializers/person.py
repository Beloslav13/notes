from django.contrib.auth.models import User
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

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
    # my_notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # read_notes = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     read_only=True
    # )

    my_notes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='note-detail'
    )

    read_notes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='note-detail'
    )

    phone = serializers.CharField(
        source='person.phone',
        allow_blank=True,
        allow_null=True
    )

    birthday = serializers.CharField(
        source='person.birthday'
    )

    last_activity = serializers.DateTimeField(
        source='person.last_activity'
    )

    person = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    count_read_notes = serializers.IntegerField(
        read_only=True
    )

    count_notes = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'url', 'person', 'last_activity', 'first_name', 'last_name', 'username', 'email',
                  'phone', 'birthday', 'my_notes', 'read_notes', 'count_notes', 'count_read_notes')

    def validate(self, data):
        attr_errors = {}
        if not data['person']['birthday']:
            attr_errors['birthday'] = _('This field has not been filled in')
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
