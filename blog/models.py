from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Post(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    post = models.TextField(null=False, blank=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=STATUS, default=0)

    def __str__(self):
        return self.post


class Comment(models.Model):
    comment = models.TextField(null=False, blank=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
