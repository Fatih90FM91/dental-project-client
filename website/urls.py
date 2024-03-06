from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('services.html', views.service, name='service'),
    path('doctors.html', views.doctor, name='doctor'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single.html', views.blogComment, name='blogComment'),
    path('appointment.html', views.appointment, name='appointment'), 
    path('register.html', views.RegisterView.as_view(), name='register'), 
    path('google_map.html', views.map, name='map'),
]
