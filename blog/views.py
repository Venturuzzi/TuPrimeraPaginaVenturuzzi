from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Category, Author
from .forms import PostForm, CategoryForm, AuthorForm, SearchForm

def home(request):
    posts = Post.objects.select_related('author', 'category')[:5]
    return render(request, 'blog/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.select_related('author', 'category').all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'blog/category_create.html', {'form': form})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'blog/author_create.html', {'form': form})

def search(request):
    form = SearchForm(request.GET or None)
    results = []
    query = ''
    if form.is_valid():
        query = form.cleaned_data.get('q') or ''
        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).select_related('author', 'category')
    return render(request, 'blog/search_results.html', {'form': form, 'results': results, 'query': query})
