from rest_framework import serializers
from details.models import student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'