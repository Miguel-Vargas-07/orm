############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
from datetime import datetime, timedelta
from faker import Faker
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *
import random 

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

"""
In case you need to start over. 
Note- this will delete any other tables on the public schema.
Alternatively, you could drop django's tables one-by-one

Login to psql and run these commands in order:

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres, public;

... then migrate again, and re-create your superuser
"""

# Seed a few users in the database
##User.objects.create(name='Dan')
##User.objects.create(name='Robert')

for u in User.objects.all():
    print(f'ID: {u.id} \tUsername: {u.name}')

award_categories = ["Best Actor", "Best Director", "Best Picture", "Lifetime Achievement", "Best Innovation"]
book_name = ["Eternity", "Alchemy", "Starlit", "Echoes", "Obsidian", "Chronicles", "Whispers", "Clockwork", "Legends", "Infinity", "Glacier", "Abyss", "Iron Sea", "Ember", "Tides"]
book_genre_ = ["Fantasy", "Mystery", "Romance", "Science Fiction", "Historical Fiction", "Thriller", "Biography", "Self-Help", "Horror", "Adventure"]

myfake = Faker()

from faker import Faker

##for i in range(10):
  ##  LibraryCard.objects.create(issue_id=myfake.date_between(start_date='2023-01-02', end_date= '2023-02-02')) ##(1/2/2023,2/2/2023))

##for i in range(10):
  ##  LibraryCard.objects.create(expiration_id=myfake.date_between(start_date='2023-02-03', end_date='2023-03-02'))  ##(2/3/2023,3/2/2023))

for i in range(10):
    User.objects.create(
        username=myfake.user_name,
        password=myfake.password,
        email=myfake.email,
        name=myfake.name
    )

start_date = datetime.strptime('2023-02-03', '%Y-%m-%d')
end_date = datetime.strptime('2023-04-05', '%Y-%m-%d')
due_date_start = datetime.strptime('2023-03-04', '%Y-%m-%d')
due_date_end = datetime.strptime('2023-04-05', '%Y-%m-%d')

if not Book.objects.exists():
    for i in range(10):
        Book.objects.create(
            book_name=random.choice(book_name),
            book_genre=random.choice(book_genre_),
            accessible=random.choice([True, False])
        )

# Get a list of all books to assign randomly
books = list(Book.objects.all())

# Loop to create Loan objects
for i in range(10):
    Loan.objects.create(
        takeout_date=myfake.date_between(start_date=start_date, end_date=end_date),
        due_date=myfake.date_between(start_date=due_date_start, end_date=due_date_end),
        book=random.choice(books)  # Assign a random book to the loan
    )


##for i in range(10):
  ##  Loan.objects.create(
    ##    takeout_date=myfake.date_between(start_date=start_date, end_date=end_date),
      ##  due_date=myfake.date_between(start_date=due_date_start, end_date=due_date_end)
    ##)
### for i in range(10):
  ##Loan.objects.create(takeout_date = myfake.date_between(
    ##start_date=datetime.strptime('2023-02-03', '2023-02-04'),
    ##end_date=datetime.strptime('2023-04-05', '2023-04-06')
##)
  ##  )


for i in range(10):
    Author.objects.create(
        author_name=myfake.name,
        award=random.choice(award_categories)
     )

##for i in range(10):
  ##  Loan.objects.create(
    ##    takeout_date=myfake.date_between(start_date='2023-02-03',end_date='2023-04-05'),
      ##  due_date=myfake.date_between(start_date='2023-03-04',end_date='2023-04-05')
    ##)

##for i in range(10):
  ##  book.objects.create(
  ##     book_name= random.choice(book_name),
   ##     book_genre= random.choice(book_genre_),
     ##   accessible= random.choice([True,False])
    ##)
    


