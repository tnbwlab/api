from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    owners = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'quantity', 'owners']