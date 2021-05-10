from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

# Create your views here.
def home(request):
    context = {'posts':posts,'title':'home page'}
    return render(request, 'blog/home.html',context);

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name ='posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    context_object_name ='post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin ,LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(UserPassesTestMixin ,LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request,'blog/about.html',context={'title':'about page'})
