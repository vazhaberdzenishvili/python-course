from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from .permissions import has_book_add_permission, has_book_delete_permission
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)


def book_list(request):
    title_query = request.GET.get('search_by_title')
    genre_query = request.GET.get('search_by_genre')

    logger.warning(f"Filtering: Title - {title_query}, Genre - {genre_query}")
    filters = Q()

    if title_query:
        filters |= Q(title__icontains=title_query)

    if genre_query:
        filters |= Q(genre__icontains=genre_query)

    if title_query and genre_query:
        filters &= Q(title__icontains=title_query) & Q(
            genre__icontains=genre_query)

    if filters:
        books = Book.objects.filter(filters)
    else:
        books = Book.objects.all()

    logger.info(f"Book Count: {books.count()}")

    return render(request, 'book/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    logger.info(f"Accessed Book detail: {book.title}, ID={pk}")

    return render(request, 'book/book_detail.html', {'book': book})


@has_book_add_permission
def add_book(request):

    logger.info("Accessed 'Add Book' page")

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save()
            logger.info(f"Added book: Title={book.title}, ID={book.id}")

            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'book/add_book.html', {'form': form})


def update_book(request, pk):
    logger.info(f"Accessed 'Update Book' page - Book ID: {pk}")
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            book = form.save()
            logger.info(f"Updated book: Title={book.title}, ID={book.id}")
            return redirect('book_detail', pk=pk)
    else:
        form = BookForm(instance=book)

    return render(request, 'book/update_book.html', {'form': form, 'book': book})


@has_book_delete_permission
def delete_book(request, pk):
    logger.info(f"Attempting to delete book - Book ID: {pk}")

    book = get_object_or_404(Book, pk=pk)
    book.delete()
    logger.info(f"Deleted book - Book ID: {pk}")

    return redirect('book_list')
