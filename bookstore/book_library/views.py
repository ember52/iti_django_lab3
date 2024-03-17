from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from book_library.models import Books, Author
from book_library.forms import BookModelForm,AuthorModelForm


def index(request):
    return HttpResponse(Books)


def home(request):
    return render(request, 'book_library/home.html')


def all_books(request):
    books = Books.objects.all()
    return render(request, 'book_library/all_books.html', context={"books": books})


def book_data(request, id):
    book = Books.objects.get(id=id)
    return render(request, 'book_library/book_info.html', context={"book": book})


def create_books(request):
    form = BookModelForm()
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            url = reverse("books")
            return redirect(url)

    return render(request, 'book_library/add_book.html', context={"form":form})


def book_delete(request, id):
    Book = Books.objects.get(id=id)
    Book.delete()
    return redirect('books')


def update_books(request, id):
    book=Books.get_book_by_id(id)
    form = BookModelForm(instance=book)
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()

            url = reverse("books")
            return redirect(url)

    return render(request, 'book_library/update_book.html', context={"form":form})






#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================


def all_authors(request):
    authors = Author.get_authors()
    return render(request, 'authors/all_authors.html', context={"authors": authors})


def author_data(request, id):
    author=Author.get_author(id)
    return render(request, 'authors/author_info.html', context={"author": author})


def create_author(request):
    form = AuthorModelForm()
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()
        
            return redirect(author.show_url)

    return render(request, 'authors/add_author.html', context={"form":form})


def author_delete(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('authors')


def update_author(request, id):
    author=Author.get_author(id)
    form = AuthorModelForm(instance=author)
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            author = form.save()

            url = reverse("authors")
            return redirect(url)

    return render(request, 'author/update_author.html', context={"form":form})
