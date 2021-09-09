from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Language(models.Model):
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)
    publication_date = models.DateField()
    description = models.CharField(max_length=400, null=True, blank=True)
    cover = models.ImageField(default='kirja.jpg', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    on_loan = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Loan(models.Model):
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    start_date = models.DateField()
    returning_date = models.DateField()     