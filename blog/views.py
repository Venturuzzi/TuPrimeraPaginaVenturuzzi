from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Resource
from .forms import PostForm, CategoryForm, AuthorForm, SearchForm, ResourceForm

def home(request):
    posts = Post.objects.select_related('author', 'category')[:5]
    return render(request, 'blog/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.select_related('author', 'category').all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/post_create.html', {'form': form})

def create_category(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/category_create.html', {'form': form})

def create_author(request):
    form = AuthorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/author_create.html', {'form': form})

def search(request):
    form = SearchForm(request.GET or None)
    results = []
    query = ''
    if form.is_valid():
        query = form.cleaned_data.get('q') or ''
        if query:
            results = Post.objects.select_related('author', 'category').filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
    return render(request, 'blog/search_results.html', {'form': form, 'results': results, 'query': query})

# --- NUEVO: Documentos/Recursos ---
def resource_list(request):
    resources = Resource.objects.select_related('author', 'category').all()
    return render(request, 'blog/resource_list.html', {'resources': resources})

def create_resource(request):
    form = ResourceForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('resource_list')
    return render(request, 'blog/resource_create.html', {'form': form})
