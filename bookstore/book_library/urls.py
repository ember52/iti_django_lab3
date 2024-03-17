from django.urls import path
from book_library.views import index, all_books, book_data, home, create_books, book_delete, update_books, all_authors, author_data
from book_library.views import *

urlpatterns = [
    path('', index, name='za3bolla'),
    path('home', home, name='hambolla'),
    path('all_books', all_books, name='books'),
    path('book<int:id>', book_data, name='book'),
    path("create_books", create_books, name="create_book"),
    path("update_books<int:id>", update_books, name="update_book"),
    path("delete_book<int:id>", book_delete, name="delete_book"),


    path("all_authors", all_authors, name="authors"),
    path('author<int:id>', author_data, name='author'),
    path("create_author", create_author, name="create_author"),
    path("update_author<int:id>", update_author, name="update_author"),
    path("delete_author<int:id>", author_delete, name="delete_author"),
]
