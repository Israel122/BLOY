from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from posts.models import Comment, Message
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class HomePageView(TemplateView):
    template_name = "posts/home.html"

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = "posts/message_create.html"
    fields = ["title","message", "picture"]


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "posts/messages.html"
    context_object_name = "posts"

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "posts/message_detail.html"
    context_object_name = "post"

class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "posts/add_comment.html"
    fields = '__all__'
    success_url = reverse_lazy("messages")


def add_likes(request, *args, **kwargs):
    post=get_object_or_404(Message,pk=kwargs.get('pk'))
    post.likes.add(request.user)
    context={'post':post}
    return redirect('message_detail', pk=kwargs.get('pk'))

