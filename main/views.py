from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core import mail
from main.models import Product
# Create your views here.


def index(request):
	return render(request, 'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def service(request):
	return render(request, 'main/service.html')

def product(request):
	results = Product.objects.all()
	print(results)
	content = {'results':results}
	return render(request,'main/product.html',content)

def photo(request):
	return render(request, 'main/photo.html')

def project(request):
	return render(request, 'main/project.html')

def detail(request,pk):
	data = Product.objects.filter(pk =pk)
	content = {'data':data}
	return render(request, 'main/detail.html',content)


def contact(request):
	if request.method == "POST":
		name= request.POST['name']
		email= request.POST['email']
		message = request.POST['message']
		send_mail(name, message, email,['hotela1707@gmail.com'], )
		return render(request, 'main/contact.html',{'name':name})
	else:
		return render(request, 'main/contact.html')
