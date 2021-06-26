from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):

    class Meta:
        verbose_name_plural = "Reviews"

    review = models.TextField(null=True, blank=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)])

    def __str__(self):
        return self.review
