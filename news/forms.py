from django.core.exceptions import ValidationError

from .models import *
from django import forms


class NewsForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории',
                                      empty_label='Категория не выбрана',
                                      )

    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5, }
            )
        }

