from rest_framework import serializers

from app.models import Obj1Ai, Obj2Ai


class Ai1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Obj1Ai
        fields = '__all__'


class Ai2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Obj2Ai
        fields = '__all__'


