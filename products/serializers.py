from rest_framework import serializers
from .models import Product

class ProducrsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = (
        #     'description',
        #     'price',
        #     'quantity'
        # )