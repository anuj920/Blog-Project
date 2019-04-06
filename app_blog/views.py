from django.shortcuts import render,get_object_or_404,redirect
from django import http
from django.utils import timezone
from app_blog.models import Post,Comment
from app_blog.forms import PostForm,CommentForm,CommentAddForm
from django.urls import reverse_lazy
from  django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class OwnPostList(ListView):
    model = Post
    template_name = 'app_blog/own_post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=False,author=self.request.user).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'app_blog/post_detail.html'
    form_class = PostForm
    model = Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'app_blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

    def delete(self, request, *args, **kwargs):
        # the Post object
        self.object = self.get_object()
        if self.object.author == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return http.HttpResponseRedirect(success_url)
        else:
            return http.HttpResponseForbidden("<h1 style='color:red;text-align:center'>Cannot delete other's posts</h1>")

class DraftListView(ListView,LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'app_blog/post_list.html'
    template_name = 'app_blog/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True,author=self.request.user).order_by('created_date')



#### Comment Add If user is login

###################################################################################
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_list')

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'app_blog/comment_form.html',{'form':form})


@login_required
def addcomment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentAddForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentAddForm()
    return render(request,'app_blog/comment_form.html',{'form':form})


def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=comment_pk)


@login_required
def like(request,pk):
    post = get_object_or_404(Post,pk=pk)
    user = request.user
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('post_detail',pk=post.pk)