from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHome.as_view()),
    path('category<int:cat_id>/', views.NewsCategories.as_view(), name='news_category'),
    path('category/<int:cat_id>/', views.NewsCategories.as_view(), name='news_category'),
]