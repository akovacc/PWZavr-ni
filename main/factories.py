import factory
from factory.django import DjangoModelFactory
from main.models import *


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    # General
    name = factory.Faker("first_name")  
    surname = factory.Faker("last_name")
    email = factory.Faker("free_email")
    phone_number = factory.Faker("phone_number")
    
    

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    category_name = factory.Faker("sentence", nb_words=2)



class NewsFactory(DjangoModelFactory):
    class Meta:
        model = News
	# General
    title = factory.Faker("sentence", nb_words=5)
    content = factory.Faker("sentence", nb_words=250)
    publication_date = factory.Faker("date_time")

    author = factory.Iterator(Author.objects.all())
    category_name = factory.Iterator(Category.objects.all())




