from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewsForm, RegisterUserForm, LoginUserForm, ContactForm
from .models import News, Category


class NewsHome(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2
    extra_context = {
        'title': 'Список новостей',
        'categories': Category.objects.all(),
    }

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsCategories(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['cat_id'], is_published=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['cat_id'])
        context['categories'] = Category.objects.all()
        context['selected_category'] = Category.objects.get(pk=self.kwargs['cat_id'])
        return context


class ShowNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'item'
    slug_url_kwarg = 'news_id'

    def get_object(self, queryset=None):
        return get_object_or_404(News.objects.all(), pk=self.kwargs[self.slug_url_kwarg])


class AddNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')
    raise_exception = True


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'news/register.html'
    extra_context = {
        'title': "Регистрация",
    }
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Регистрация прошла успешно! Теперь вы можете войти.")
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'news/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class ContactFormView(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = 'news/contact.html'
    success_url = reverse_lazy('home')
    title_page = 'Обратная связь'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        content = form.cleaned_data['content']

        send_mail(
            subject=subject,
            message=content,
            from_email='no-reply@example.com',
            recipient_list=['recipient@example.com'],
        )

        print(self.request._messages)
        messages.success(self.request, "Письмо отправлено.")

        return super().form_valid(form)
