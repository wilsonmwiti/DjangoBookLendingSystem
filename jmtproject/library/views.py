from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Book, Author, Category, Loan
from django.db.models import Q
from .forms import LoanForm
import datetime
from .filters import BookFilter


def index(request):
    """View function for home page of site."""

    book = Book.objects.all()
    author = Author.objects.all()
    category = Category.objects.all()
    newbook = Book.objects.order_by('-publication_date')[:4]

    myFilter = BookFilter(request.GET, queryset=book)
    book = myFilter.qs

    context = {
        'book' : book,
        'author' : author,
        'category' : category,
        'newbook' : newbook,
        'myFilter' : myFilter,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'library/books.html', context=context)


def book_view(request, pk):
    book = Book.objects.get(pk=pk)
    data = {
        'returning_date': datetime.date.today() + datetime.timedelta(days=14)
    }
    if request.method == 'POST' and book.on_loan == False:
        loan_form = LoanForm(request.POST, initial=data)
        if loan_form.is_valid():
            new_loan = Loan.objects.create(
                borrower = request.user,
                start_date = datetime.date.today(),
                returning_date = datetime.date.today() + datetime.timedelta(days=14),
                borrowed_book = book
            )
            book.on_loan = True
            book.save()
            new_loan.save()
    else:
        loan_form = LoanForm(initial=data)

    is_on_loan = Loan.objects.filter(borrowed_book=book, returning_date__gt=datetime.date.today())
    if len(is_on_loan) > 0:
        loan_info = {
            'available': False,
            'return_date': is_on_loan[0].returning_date
        }
    else:
        loan_info = {
            'available': True
        }

    context = {
        'loan_form': loan_form,
        'book': book,
        'loan_info': loan_info
    }
    template = 'library/book.html'

    return render(request, template, context)

# Searchbar
def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        book = Book.objects.filter(
            Q(title__icontains=q) |
            Q(authors__first_name__icontains=q) |
            Q(authors__last_name__icontains=q) |
            Q(publisher__name__icontains=q) |
            Q(description__icontains=q) |
            Q(language__language__icontains=q)
        )
        context = {
            'query' : q,
            'book' : book
        }
        template = 'library/search.html'
    else:
        # if user just hits only the enter, this message will appear
        message = " "
        context = {
            'query' : message,
        }
        template = 'library/search.html'

    return render(request, template, context=context)

