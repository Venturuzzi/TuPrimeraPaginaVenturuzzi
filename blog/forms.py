from django import forms
from .models import Post, Category, Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'author']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

class SearchForm(forms.Form):
    q = forms.CharField(label='Buscar', max_length=100, required=False,
                        widget=forms.TextInput(attrs={'placeholder': 'Título o contenido'}))
