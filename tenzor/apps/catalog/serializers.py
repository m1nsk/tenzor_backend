from rest_framework import serializers
from .models import Category, Goods
import os


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'id')


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = ('name', 'qty', 'price', 'production_date', 'category', 'id')





