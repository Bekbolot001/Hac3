from rest_framework import serializers
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        book = Books.objects.create(**validated_data)
        book.save()
        return book

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('book', 'year', 'image')