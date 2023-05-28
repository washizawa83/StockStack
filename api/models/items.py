import os
from django.db import models


def image_url(instance, filename):
    return os.path.join('items', f'{instance.id}_{filename}')


class Tag(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to=image_url, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField(blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image
        else:
            return '/items/no_image.gif'

