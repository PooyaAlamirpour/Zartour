from rest_framework import serializers
from tickets.models import Airport


class AirportSerializer(serializers.Serializer):
    country= serializers.CharField(required=False, allow_blank=True, max_length=100)
    en_country= serializers.CharField(required=False, allow_blank=True, max_length=100)
    name= serializers.CharField(required=False, allow_blank=True, max_length=100)
    en_name= serializers.CharField(required=False, allow_blank=True, max_length=100)
    airport= serializers.CharField(required=False, allow_blank=True, max_length=100)
    iata=serializers.CharField(required=True, allow_blank=False, max_length=100)
    lat= serializers.CharField(required=False, allow_blank=True, max_length=20)
    lng= serializers.CharField(required=False, allow_blank=True, max_length=20)
    order= serializers.CharField(required=False, allow_blank=True, max_length=20)
    id = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    def get_id(self, obj):
        return '{"code":"'+obj.iata+'","label":"'+obj.en_name+'"}'

    def get_text(self, obj):
        return obj.airport + " " + obj.name

    def create(self, validated_data):
        """
        Create and return a new `Airport` instance, given the validated data.
        """
        return Airport.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Airport` instance, given the validated data.
        """
        instance.country = validated_data.get('country', instance.country)
        instance.en_country = validated_data.get('en_country', instance.en_country)
        instance.name = validated_data.get('name', instance.name)
        instance.en_name = validated_data.get('en_name', instance.en_name)
        instance.airport = validated_data.get('airport', instance.airport)
        instance.iata = validated_data.get('iata', instance.iata)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lng = validated_data.get('lng', instance.lng)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance
