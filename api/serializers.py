from rest_framework import serializers

from App_Shop.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # ('__all__')  for all fields
        # ['quote', 'author']
        # fields = ['quote', 'author']
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # ('__all__')  for all fields
        # ['quote', 'author']
        # fields = ['quote', 'author']
        fields = ('__all__')


