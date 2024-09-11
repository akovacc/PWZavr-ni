
from django.db import models

class News(models.Model):
	title = models.CharField("Naslov", max_length=25, primary_key=True)
	content = models.TextField("Tekst članka", blank = True, null = True)
	publication_date = models.DateField("Datum objave", blank = True, null = True)

	#Vanjski kljucevi
	author = models.ForeignKey("Author", verbose_name="Author", on_delete=models.CASCADE, blank = True, null = True)
	category_name = models.ForeignKey("Category", verbose_name="Category", on_delete=models.CASCADE, blank = True, null = True)

	def __str__(self):
		return self.title
	



class Author(models.Model):

	name = models.CharField("Ime", max_length=64)
	surname = models.CharField("Prezime", max_length=64)
	email = models.EmailField("Email", blank=True, null=True)
	phone_number = models.CharField("Broj telefona", max_length = 10, blank = True, null = True)

	def __str__(self):
		return self.surname + " " +self.name
		

class Category(models.Model):
	category_name = models.CharField("Naziv kategorije", max_length=128)

	def __str__(self):
		return self.category_name

