from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .error.error_views import TypeModelError, EventModelError, PersonModelError
from .models import Type, Event, Person
from .serializers import TypeSerializer, TypeDetailSerializer, EventDetailSerializer, PersonDetailSerializer


class TypeView(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = TypeModelError()

    @action(methods=['get'], detail=False)
    def get_types(self, request):
        return Response(
            self.serializer_class(self.queryset, many=True).data,
            status=status.HTTP_200_OK,
        )


class TypeDetailView(viewsets.ModelViewSet):
    serializer_class = TypeDetailSerializer
    queryset = Type.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = TypeModelError()

    @action(methods=['get'], detail=False)
    def get_detail_type(self, request, pk):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()
        return Response(
            self.serializer_class(qs[0]).data,
            status=status.HTTP_200_OK,
        )


class EventDetailView(viewsets.ModelViewSet):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = EventModelError()

    @action(methods=['get'], detail=False)
    def get_detail_event(self, request, pk):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()
        return Response(
            self.serializer_class(qs[0], context={'limit': 8}).data,
            status=status.HTTP_200_OK,
        )


class PersonDetailView(viewsets.ModelViewSet):
    serializer_class = PersonDetailSerializer
    queryset = Person.objects.all()
    permission_classes = [permissions.AllowAny]
    error_helper = PersonModelError()

    @action(methods=['get'], detail=False)
    def get_detail_person(self, request, pk):
        qs = self.queryset.filter(pk=pk)
        if len(qs) == 0:
            return self.error_helper.is_not_found()
        return Response(
            self.serializer_class(qs[0]).data,
            status=status.HTTP_200_OK,
        )
