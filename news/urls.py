from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHome.as_view(), name='home'),
    path('category/<int:cat_id>/', views.NewsCategories.as_view(), name='category'),

]