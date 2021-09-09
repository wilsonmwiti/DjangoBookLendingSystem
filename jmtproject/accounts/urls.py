from django.urls import path
from .views import RegistrationView, user_detail_view
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('profile/<int:pk>', login_required(user_detail_view), name='profile'),
]