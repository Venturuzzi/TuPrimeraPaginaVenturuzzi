from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from .forms import PageForm


class PageListView(ListView):
    model = Page
    template_name = 'blogpages/page_list.html'
    context_object_name = 'page_list'


class PageDetailView(DetailView):
    model = Page
    template_name = 'blogpages/page_detail.html'
    context_object_name = 'page'


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'blogpages/page_form.html'
    success_url = reverse_lazy('blogpages:page_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'blogpages/page_form.html'
    success_url = reverse_lazy('blogpages:page_list')


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'blogpages/page_confirm_delete.html'
    success_url = reverse_lazy('blogpages:page_list')



def about_view(request):
    return render(request, 'blogpages/about.html')
