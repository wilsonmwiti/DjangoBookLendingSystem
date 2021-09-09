import django_filters
from .models import *

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = [
            'authors',
            'publisher',
            'language',
            'category',
            ]