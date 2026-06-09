from django import forms
from django.core.validators import MinLengthValidator
from .models import Post, Category

class PostForm(forms.ModelForm):
    content = forms.CharField(
        label="Содержание поста",
        widget=forms.Textarea(attrs={'rows': 6}),
        validators=[MinLengthValidator(50, message="Содержание должно содержать минимум 50 символов")]
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        labels = {
            'title': 'Заголовок',
            'category': 'Категория',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
        labels = {
            'title': 'Название категории',
            'description': 'Описание',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }