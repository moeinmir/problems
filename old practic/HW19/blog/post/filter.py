
import django_filters

from .models import *


class PostListFilter(django_filters.FilterSet):
    # creator_isnull = django_filters.BoleanFilter(field_name='creator', lookup_expr='isnull')
    # filter_fields = {
    #     'likes': ['gte', 'lte']
    # }

    class Meta:
        model = Post

        fields = {
            'post_title': ['exact']
        }
