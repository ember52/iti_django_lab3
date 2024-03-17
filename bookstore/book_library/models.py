from django.db import models
from django.shortcuts import reverse, get_object_or_404


class Author (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    bdate = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return f'/media/{self.image}'
    @property
    def edit_url(self):
        url = reverse('update_author', args=[self.id])
        return url
    @property
    def show_url(self):
        url = reverse('author', args=[self.id])
        return url
    
    @classmethod
    def get_authors(cls):
        return cls.objects.all()
    
    @classmethod
    def get_author(cls,id):
        return get_object_or_404(cls,id=id)
    



#=======================================================================


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100)
    authorname = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
    image = models.ImageField(upload_to='images/', null=True)
    pages = models.IntegerField(default=10, null=True)
    price = models.FloatField(default=10, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)  # create
    updated_at = models.DateTimeField(auto_now=True, null=True)  # update

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return f'/media/{self.image}'

    @property
    def show_url(self):
        url = reverse('book', args=[self.id])
        return url

    #     path('book<int:id>', book_data, name='book'),

    @property
    def edit_url(self):
        url = reverse('update_book', args=[self.id])
        return url

    #    path("update_books<int:id>", update_books, name="update_book"),

    @classmethod
    def create_object(cls, name, author, image, pages, price):
        try:
            book = cls(name=name, author=author,image=image,pages=pages,price=price)
            print(name, author, image, pages, price)
            book.save()
        except Exception as e:
            print(e)
            return False
        else:
            return book


    @classmethod
    def get_book_by_id(cls, id):
        return get_object_or_404(cls, id=id)


#------------------------------------------------------------------------------------------------------------


