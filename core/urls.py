from django.contrib import admin
from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('books/', core.views.Books.as_view(), name='book_list'),
    path('books/<int:pk>/', core.views.BookDetail.as_view(), name='book_detail'),
]
