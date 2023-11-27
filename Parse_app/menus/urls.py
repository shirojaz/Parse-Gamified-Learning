from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = "Home Page"),
    path('account/', views.homepage, name = 'empty link brah'),
    path('account/create', views.createAccount, name = 'Account Creation'),
    path('index/', views.index, name= 'Index'),
    path('courses/', views.courses, name = 'Courses'),
]
