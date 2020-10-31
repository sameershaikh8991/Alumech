#from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
#fs = FileSystemStorage(location='/media/pdf/')
class Product(models.Model):
	head_name = models.CharField(max_length=100)
	desc = models.TextField(max_length=5000)
	#date =  models.DateField()
	image=models.ImageField(upload_to="main/images",default="")

	def __str__(self):
		return self.head_name
