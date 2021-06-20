from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):

    class Meta:
        verbose_name_plural = "Reviews"

    title = models.CharField(max_length=50, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    posted_by = ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])

    def __str__(self):
        return self.review
