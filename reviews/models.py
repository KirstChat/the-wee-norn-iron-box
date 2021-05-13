from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

# Create your models here.


class Review(models.Model):

    class Meta:
        verbose_name_plural = "Reviews"

    user = OneToOneField(User, on_delete=models.CASCADE)
    review = models.TextField(null=True, blank=True)
    dated_added = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.review
