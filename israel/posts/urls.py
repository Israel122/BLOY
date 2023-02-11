from django.urls import path
from posts.views import HomePageView, MessageCreateView, MessageDetailView, MessageListView, AddComment
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("messages/create/", MessageCreateView.as_view(), name="message_create"),
    path("messages/", MessageListView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("add comments/", AddComment.as_view(), name="add comments"),
    path("likes/<int:pk>/", views.add_likes, name="likes")
]