from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

# Create your models here.
User = get_user_model()


class Tag(models.Model):

    name = models.CharField(max_length=100)


class Category(models.Model):
    category_name = models.CharField(max_length=72)

    def __str__(self):
        return self.category_name


class Post(models.Model):

    title = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    creator = models.ForeignKey(
        User, related_name='posts', on_delete=CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    tag = models.ForeignKey(Tag, on_delete=CASCADE, related_name='s_post')
    post_category = models.ManyToManyField(Category, null=True, blank=True)


class Comment(models.Model):
    comment_content = models.CharField(max_length=255)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_content
