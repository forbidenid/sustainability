from django.urls import path
from sustainability import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name="about"),
    path('portfolio', views.portfolio,name="portfolio"),
    path('contact/',views.contactus,name='contactus'),
    
]