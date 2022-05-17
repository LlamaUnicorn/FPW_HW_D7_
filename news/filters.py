from django_filters import FilterSet, DateFilter
from .models import Post
# import django_filters
# from django.db import models
from django import forms


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.


# class PostFilter(FilterSet):
#     time_in = DateFilter(
#         lookup_expr='gt',
#         widget=forms.DateInput(
#             attrs={
#                 'type': 'date'
#             }
#         )
#     )
#
#     class Meta:
#         # В Meta классе мы должны указать Django модель,
#         # в которой будем фильтровать записи.
#         model = Post
#         # В fields мы описываем по каким полям модели
#         # будет производиться фильтрация.
#         fields = {
#             # поиск по названию
#             'title': ['icontains'],
#             'dateCreation': ['lt', 'gt'],
#             'postCategory': ['exact'],
#         }


class PostFilter(FilterSet):
    dateCreation = DateFilter(
        lookup_expr='gt',
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Post
        fields = {
            # поиск по названию
            'title': ['icontains'],
            'author': ['exact'],
            # 'dateCreation': ['lt', 'gt'],
            'postCategory': ['exact'],
            'categoryType': ['exact']
        }
