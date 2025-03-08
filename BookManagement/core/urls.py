from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/add/', views.CreateBookView.as_view(), name='add_book'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete_book'),
    path('book/update/<int:pk>/', views.BookUpdateView.as_view(), name='update_book'),
    path('book/buy/<int:pk>/', views.BookPurchaseView.as_view(), name='buy_book')
]
