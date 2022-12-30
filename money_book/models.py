from django.db import models
from user.models import User


class Post(models.Model):
    expense = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.expense}원 - {self.description}"
