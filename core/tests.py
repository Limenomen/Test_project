from django.test import TestCase, Client
from django.urls import reverse

from core import models


class BookModel(TestCase):

    def setUp(self):
        self.book = models.Book.objects.create(name='Test Book')

    def testStr(self):
        self.assertEqual(
            str(self.book),
            'Test Book',
        )


class BookSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.book1 = models.Book.objects.create(name='Test Book 1')
        self.book2 = models.Book.objects.create(name='Test Book 2')

    def testWithoutParams(self):
        response = self.client.get(reverse('core:book_list'))
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Book.objects.all()),
            'При поиске без параметров должны выводиться все книги',
        )

    def testSearchByName(self):
        response = self.client.get(reverse('core:book_list'), data={'name': 'Test Book 1'})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Test Book 1',
            response.context['object_list'].first().name,
        )