from django.urls import reverse
from django.db import models

from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="image/", blank=True, null=True)
    likes = models.ManyToManyField(user, related_name="likes")

    def num_of_likes(self):
        return self.likes.count()
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("message_detail", args=[str(self.id)])
        return reverse("messages")


class Comment(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    message = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Message, related_name="name", on_delete=models.CASCADE)

    def __str__(self):
        return self.message
