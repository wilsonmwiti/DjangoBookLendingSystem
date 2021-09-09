from django.contrib import admin
from .models import Book, Author, Loan, Publisher, Language, Category
import datetime
# Register your models here.

class LoanAdmin(admin.ModelAdmin):

    list_display = ('borrower', 'borrowed_book', 'start_date', 'returning_date')
    list_filter = ('borrower', 'borrowed_book')

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Publisher)
admin.site.register(Language)
admin.site.register(Category)

#admin view site url
admin.site.site_url = "/library"