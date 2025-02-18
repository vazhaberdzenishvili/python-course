from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="books", null=True, blank=True)
    published_year = models.IntegerField(null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.author}"
