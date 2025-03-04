from django.db import models
from django.contrib.auth.models import User

GENRES = (
    ("fiction", "Fiction"),
    ("nonfiction", "Non-Fiction"),
    ("mystery", "Mystery"),
    ("scifi", "Science Fiction"),
    ("fantasy", "Fantasy"),
    ("biography", "Biography"),
)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="books", null=True, blank=True)
    genre = models.CharField(max_length=20, choices=GENRES, blank=True)
    published_year = models.IntegerField(null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    book_count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def is_sold_out(self):
        if self.book_count <= 0:
            return True
        else:
            return False


class BookCart(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='books')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='books')
    book_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('book', 'user')
