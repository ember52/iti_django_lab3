from django import forms
from book_library.models import Books,Author

class AuthorModelForm (forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters ")
        if Author.objects.filter(name=name).exists():
            raise forms.ValidationError("name already exists")
        return name


class BookModelForm (forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters ")
        if Books.objects.filter(name=name).exists():
            raise forms.ValidationError("name already exists")
        return name

    def clean_author(self):
        author = self.cleaned_data['name']
        if len(author) < 2:
            raise forms.ValidationError("author name must be at least 2 characters ")
        return author

    def clean_page(self):

        pages = self.cleaned_data['pages']
        if not pages.isdigit():
            raise forms.ValidationError("number of pages must be a positive integer!")
        if pages <= 0:
            raise forms.ValidationError("number of pages must be a positive integer!")
        return pages

    def clean_price(self):

        price = self.cleaned_data['price']
        try:
            price = float(price)
            if price <= 0:
                raise forms.ValidationError("Price must be a positive number!")
        except ValueError:
            raise forms.ValidationError("Price must be a positive number!")
        return price

#========================================================================================================



    


