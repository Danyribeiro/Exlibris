from django import forms
from django.forms import ModelForm
from .models import Book

class DateInput(forms.DateInput):
    input_type ="date"


class BookForm (forms.ModelForm):
  title = forms.CharField(label="Título")
  author = forms.CharField(label="Autor")
  publisher = forms.CharField(label="Editora")
  publisher_date = forms.DateField(label="Data de publicação", widget=DateInput())
  pages = forms.CharField(label="Páginas")
  isbn = forms.CharField(label="ISBN")
  classification = forms.CharField (label="Classificação")

  class Meta:
        model = Book
        fields = (
              "title",
              "author",
              "publisher",
              "publisher_date",
              "pages",
              "isbn",
              "classification"
              )


      