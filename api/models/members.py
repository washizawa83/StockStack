import os
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def image_url(instance, filename):
    return os.path.join('members', f'{instance.name}_{filename}')


class MemberGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to=image_url)
    group = models.ForeignKey(MemberGroup, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name
