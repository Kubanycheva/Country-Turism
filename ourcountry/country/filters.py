from django_filters import rest_framework as filters, CharFilter
from datetime import datetime
from .models import *


class PopularReviewFilter(filters.FilterSet):
    # Фильтр по рейтингу
    rating = filters.ChoiceFilter(choices=[
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ])

    # Фильтр по месяцам
    month = filters.ChoiceFilter(
        method='filter_month',
        choices=[
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
        ]
    )

    def filter_month(self, queryset, name, value):
        return queryset.filter(created_date__month=value)

    class Meta:
        model = PopularReview
        fields = ['rating', 'month']


class KitchenReviewFilter(filters.FilterSet):
    # Фильтр по рейтингу
    rating = filters.ChoiceFilter(choices=[
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ])

    # Фильтр по месяцам
    month = filters.ChoiceFilter(
        method='filter_month',
        choices=[
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
        ]
    )

    def filter_month(self, queryset, name, value):
        return queryset.filter(created_at__month=value)

    class Meta:
        model = KitchenReview
        fields = ['rating', 'month']


class HotelsReviewFilter(filters.FilterSet):
    # Фильтр по рейтингу
    rating = filters.ChoiceFilter(choices=[
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ])

    # Фильтр по месяцам
    month = filters.ChoiceFilter(
        method='filter_month',
        choices=[
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
        ]
    )

    def filter_month(self, queryset, name, value):
        return queryset.filter(created_date__month=value)

    class Meta:
        model = HotelsReview
        fields = ['rating', 'month']


class AttractionReviewFilter(filters.FilterSet):
    # Фильтр по рейтингу
    rating = filters.ChoiceFilter(choices=[
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    ])

    # Фильтр по месяцам
    month = filters.ChoiceFilter(
        method='filter_month',
        choices=[
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
        ]
    )

    def filter_month(self, queryset, name, value):
        return queryset.filter(created_date__month=value)

    class Meta:
        model = AttractionReview
        fields = ['rating', 'month']


class EventFilter(filters.FilterSet):
    # Используем CharFilter для фильтрации по полю 'category__category' (название категории)
    category = CharFilter(field_name='category__category', lookup_expr='exact')

    class Meta:
        model = Event
        fields = ['category', 'date', 'ticket']


