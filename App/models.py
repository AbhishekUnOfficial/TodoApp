from uuid import uuid1, uuid4
from django.db import models
from django.utils.text import slugify


class TodoModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    slug = models.SlugField(blank=True, null=True)
    created_time = models.TimeField(auto_now_add=True)
    updated_time = models.TimeField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{str(uuid4())[:4]}"
        super(TodoModel, self).save(*args, *kwargs)
