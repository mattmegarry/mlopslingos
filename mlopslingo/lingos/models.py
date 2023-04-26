from django.db import models


class LingoType(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Lingo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lingo_type = models.ForeignKey(LingoType, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
