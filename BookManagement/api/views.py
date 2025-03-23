from rest_framework import status
from core.models import Book
from .serializers import BookSerializer
from rest_framework.generics import  ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser
from .filters import BookFilter
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        books = super().get_queryset()
        filterset = BookFilter(self.request.query_params, queryset=books)

        if filterset.is_valid():
            books = filterset.qs
        return books

    @swagger_auto_schema(
        operation_summary='Get Book Details',
        operation_description='This endpoint returns book details with filtering and pagination',
        manual_parameters=[
            openapi.Parameter('page', openapi.IN_QUERY,
                              type=openapi.TYPE_INTEGER, description='Page number'),
            openapi.Parameter('page_size', openapi.IN_QUERY,
                              type=openapi.TYPE_INTEGER, description='Page size'),
            openapi.Parameter('title', openapi.IN_QUERY,
                              type=openapi.TYPE_STRING, description='Filter by book title'),
            openapi.Parameter('author', openapi.IN_QUERY,
                              type=openapi.TYPE_STRING, description='Filter by author name'),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successful response",
                schema=BookSerializer(many=True),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description='Invalid request',
            ),
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AddBookAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = [MultiPartParser, FormParser]


class UpdateBookAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = [MultiPartParser, FormParser]


class DeleteBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
