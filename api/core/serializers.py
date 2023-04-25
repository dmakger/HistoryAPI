from rest_framework import serializers

from .models import Type, Event, Person


# ####### ТИПЫ #######
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class TypeDetailSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = Type
        fields = '__all__'

    @staticmethod
    def get_content(instance):
        return EventSerializer(Event.objects.filter(types=instance), many=True).data


# ####### СОБЫТИЯ #######
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'image', 'title', 'description']


class EventDetailSerializer(serializers.ModelSerializer):
    persons = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'persons', 'content']

    @staticmethod
    def get_persons(instance):
        return PersonSerializer(instance.persons, many=True).data


# ####### ПЕРСОНЫ #######
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'lastname', 'username', 'pastname']


class PersonDetailSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    @staticmethod
    def get_events(instance):
        return EventSerializer(Event.objects.filter(persons=instance), many=True).data
