from rest_framework import serializers

class MultiplicationSerializer(serializers.Serializer):
  number1 = serializers.FloatField(required=True)
  number2 = serializers.FloatField(required=True)