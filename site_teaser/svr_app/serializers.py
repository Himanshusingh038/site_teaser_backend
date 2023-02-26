from rest_framework import serializers
from .models import PropertySurrounding

class PropertySurroundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertySurrounding
        fields = ('property_id', 'title', 'desc', 'distance', 'property_type')
