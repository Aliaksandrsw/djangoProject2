from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHome.as_view()),
]