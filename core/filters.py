import django_filters

import core.models


class BookFilter(django_filters.FilterSet):
    name = django_filters.Filter(lookup_expr='icontains', label='Название')

    class Meta:
        model = core.models.Book
        fields = ('name', )

