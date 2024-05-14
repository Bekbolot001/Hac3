from django.contrib import admin
from .models import Books

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'book', 'author', 'description', 'image', 'year')
    list_filter = ('manufacturer', )
    search_fields = ('model', )