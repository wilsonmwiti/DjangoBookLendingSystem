from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'library'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('books/<int:pk>', login_required(views.book_view), name='book'),
    path('search/', login_required(views.search), name='search'),
]
