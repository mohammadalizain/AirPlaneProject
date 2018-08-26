from rest_framework import serializers
from airplanes.models import airplanes 

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = airplanes
        fields = ['id', 'name', 'picture',]

class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = airplanes
        fields = '__all__'


class CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = airplanes
        fields = '__all__'



class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = airplanes
        fields = '__all__'