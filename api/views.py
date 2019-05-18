from django.shortcuts import render

# Create your views here.
from tickets.models import Airport
from tickets.serializers import AirportSerializer
from rest_framework import generics
from rest_framework import filters


class AirportList(generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('en_name', 'name', 'airport', 'iata')


class AirportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer



