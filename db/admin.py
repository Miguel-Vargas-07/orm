from django.contrib import admin

from .models import User, Reporter, Article, Publication, LibraryCard, Book, Loan, Author

admin.site.register(User)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(LibraryCard)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Author)

