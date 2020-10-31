from django.urls import path  
from . import views

urlpatterns = [
	path('',views.index, name="home"),
	path('about/',views.about, name="about"),
	path('service/',views.service, name="service"),
	path('product/',views.product, name="product"),
	path('project/',views.project, name="project"),
	path('photo/',views.photo, name="photo"),
	path('<int:pk>',views.detail, name="detail"),
	path('contact/',views.contact, name="contact"),
	]