import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)


    def __str__(self):
        return self.name


class Reporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    
def __str__(self):
        return self.headline

class Meta:
        ordering = ["headline"]

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["headline"]

class LibraryCard(models.Model):
    issue_date = models.DateField()
    expiration_date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Author (models.Model):
    author_name = models.CharField(max_length = 500)
    award = models.CharField(max_length = 100)

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_genre = models.CharField(max_length=100)
    accessible = models.BooleanField()
    author_name = models.ManyToManyField(Author)

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    takeout_date = models.DateField()
    due_date = models.DateField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)

