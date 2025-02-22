from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from .permissions import has_book_add_permission, has_book_delete_permission
from django.db.models import Q


def book_list(request):
    title_query = request.GET.get('search_by_title')
    genre_query = request.GET.get('search_by_genre')

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

    return render(request, 'book/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'book/book_detail.html', {'book': book})


@has_book_add_permission
def add_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save()

            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'book/add_book.html', {'form': form})


@has_book_delete_permission
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()

    return redirect('book_list')
