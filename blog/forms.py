from django import forms
from .models import Post, Category, Author, Resource

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
    q = forms.CharField(
        label='Buscar',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar en artículos (título o contenido)'}),
    )

# --- NUEVO ---
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'file', 'url', 'category', 'author']

    def clean(self):
        cleaned = super().clean()
        file = cleaned.get('file')
        url = cleaned.get('url')
        if not file and not url:
            raise forms.ValidationError('Cargá un archivo o indicá un enlace (al menos uno).')
        return cleaned
