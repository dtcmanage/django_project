from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # views.home tells it to look at views.py for function home; use blog-home instead of home to simplify future needs for lookup, always smart to be clear and specific
    path('about/', views.about, name='blog-about'),
    
]
