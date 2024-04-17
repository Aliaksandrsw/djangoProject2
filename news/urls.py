from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHome.as_view(), name='home'),
    path('category/<int:cat_id>/', views.NewsCategories.as_view(), name='category'),
    path('news/<int:news_id>/', views.ShowNews.as_view(), name='view_news')

]