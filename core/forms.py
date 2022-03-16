from django import forms

import core.models


class BookSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    pages = forms.IntegerField(label='Кол-во страниц', required=False, help_text='Минимальное количество страниц')

    def clean_pages(self):
        pages = self.cleaned_data.get('pages')

        if pages and pages > 1000:
            raise forms.ValidationError('Количество страниц не может быть больше 1000')

        return pages


class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'

