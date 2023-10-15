from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publisher = models.CharField(max_length=200)
  publisher_date = models.DateField()
  pages = models.CharField(max_length=30)
  isbn = models.CharField('ISBN', max_length=13,unique=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                          '">ISBN number</a>')   
  classification = models.CharField (max_length=100)

  def get_absolute_url(self):
        return reverse("catalog:catalog-update", kwargs={"id": self.id})
  
  def get_delete_url(self):
      return reverse("catalog:catalog-delete", kwargs={"id": self.id})

  def __str__(self):
      return self.title
  class Meta:
       db_table ="book"
       ordering =['id']
       

  