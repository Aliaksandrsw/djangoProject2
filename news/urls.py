from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.NewsHome.as_view(), name='home'),
    path('category/<int:cat_id>/', views.NewsCategories.as_view(), name='category'),
    path('news/<int:news_id>/', views.ShowNews.as_view(), name='view_news'),
    path('news/add_news/', views.AddNews.as_view(), name='add_news'),
    path('register/', views.RegisterUser.as_view(), name='register'),


]
