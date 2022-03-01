from django.db import models


class Book(models.Model):
    name = models.CharField('Название', max_length=128)
    pages = models.IntegerField('Количество страниц', blank=True, null=True)

    def __str__(self):
        return self.name
