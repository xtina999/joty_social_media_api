from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    hashtag = models.CharField(max_length=100)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
