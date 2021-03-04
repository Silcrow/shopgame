from django.db import models


class Merchandise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=280, null=True)
    effects = models.TextField(max_length=280, null=True)
    price = models.PositiveIntegerField(default=0)
    durability = models.PositiveIntegerField(default=1)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
