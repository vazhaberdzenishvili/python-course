from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, BookCart
from .forms import BookForm
from .permissions import has_book_add_permission, has_book_delete_permission
from django.db.models import Q
import logging
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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

    paginator = Paginator(books, 3)

    try:
        page = request.GET.get('page')
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'book/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    logger.info(f"Accessed Book detail: {book.title}, ID={pk}")

    return render(request, 'book/book_detail.html', {'book': book})


@has_book_add_permission
def add_book(request):

    logger.info("Accessed 'Add Book' page")

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

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
        form = BookForm(request.POST, request.FILES, instance=book)
        print(request.FILES)
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


def buy_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if book.is_sold_out():
        messages.error(request, 'Book not available')
        return redirect('book_list')

    item = BookCart.objects.filter(
        book=book, user=request.user).first()

    if item:
        messages.error(
            request, 'You have already added this book to your cart')
    else:
        book_cart = BookCart.objects.create(
            book=book, user=request.user, book_count=1)
        book.book_count -= 1
        book.save()
        messages.success(
            request, f'Successfully added {book.title} to your cart!')

    send_mail(
        'Book Purchase Confirmation',
        f'{request.user.username} has successfully added book: {book.title} by {book.author} to their cart.',
        settings.DEFAULT_FROM_EMAIL,
        [request.user.email],
        fail_silently=False
    )

    return redirect('book_list')
