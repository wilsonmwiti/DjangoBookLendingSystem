import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from library.models import Loan, Book
from .forms import UserDetailForm


class RegistrationView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def user_detail_view(request, pk):
    loan_list = Loan.objects.filter(borrower=request.user, borrowed_book__on_loan=True, returning_date__gt=datetime.date.today())

    if request.method == "POST":
        if request.POST.get('username'):
            form = UserDetailForm(request.POST, instance=request.user)
            if form.is_valid:
                form.save()
        elif request.POST.getlist('loan'):
            loans = request.POST.getlist('loan')
            for loan in loans:
                loan_object = Loan.objects.get(pk=loan)
                loan_object.returning_date = datetime.date.today()
                loan_object.save()
                loan_object.borrowed_book.on_loan = False
                loan_object.borrowed_book.save()
            form = UserDetailForm(instance=request.user)
        else:
            form = UserDetailForm(instance=request.user)
    else:
        form = UserDetailForm(instance=request.user)

    template = 'profile/profile.html'

    context = {
        'form': form,
        'loan_list': loan_list,
    }

    return render(request, template, context)