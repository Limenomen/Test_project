import django_filters

import core.models


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = core.models.Book
        fields = '__all__'
