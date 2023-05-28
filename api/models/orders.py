from django.db import models

from accounts.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
