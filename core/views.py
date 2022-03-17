from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

import core.models
import core.forms
import core.filters


class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Главная страница'


class Books(TitleMixin, ListView):
    title = 'Книги'

    def get_filters(self):
        return core.filters.BookFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        context['filters'] = self.get_filters()
        return context


class BookDetail(TitleMixin, DetailView):
    queryset = core.models.Book.objects.all()

    def get_title(self):
        return str(self.get_object())


class BookUpdate(TitleMixin, UpdateView):
    model = core.models.Book
    form_class = core.forms.BookEdit

    def get_title(self):
        return f'Изменение данных книги "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('core:book_list')


class BookCreate(TitleMixin, CreateView):
    model = core.models.Book
    form_class = core.forms.BookEdit
    title = 'Добавление книги'

    def get_success_url(self):
        return reverse('core:book_list')


class BookDelete(TitleMixin, DeleteView):
    model = core.models.Book

    def get_title(self):
        return f'Удаление книги {str(self.get_object())}'

    def get_success_url(self):
        return reverse('core:book_list')
