from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.BookListAPIView.as_view(), name='book_list'),
    path('book/add/', views.AddBookAPIView.as_view(), name='add_book'),
    path('book/update/<int:pk>/',
         views.UpdateBookAPIView.as_view(), name='update_book'),
    path('book/delete/<int:pk>/',
         views.DeleteBookAPIView.as_view(), name='delete_book'),
]
