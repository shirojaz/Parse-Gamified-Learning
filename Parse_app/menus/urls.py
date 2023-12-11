from django.urls import path
from . import views

urlpatterns = [
    path('', views.startpage, name = "Start Page"),
    path('dashboard/', views.index, name = "Home page"),
    path('account/', views.account, name = 'Account Settings'), # changed "views.homepage" to "views.account"
    path('signup/', views.signup, name = 'Account Creation'),
    path('account/successful/', views.successfulAccount, name = 'Account Successful'),
    path('courses/', views.courses, name = 'Courses'),

#Added
    path('about/', views.about, name = 'About Page'),
    path('error/', views.error, name = 'Error Page'),
    path('courses/finished', views.finished, name = 'Course Finished'),
    path('help/', views.help, name= 'Help Page'),
    path('login/', views.user_login, name = 'Login Page'),
    path('quizzes/', views.quiz_instance, name='Quiz Instance'),


#Second batch
    path('quizzes/questions/', views.finished, name = 'addQuestion'),
    path('quizzes/choices/', views.help, name= 'addChoices'),
    path('quizzes/questions/edit/', views.user_login, name = 'addEditQuestion'),
    path('quizzes/choices/edit/', views.quiz_instance, name='addEditChoices'),

#Third Batch
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),

#Fourth Batch
    path('test/typeb/', views.quiz_typeB, name="Test Quiz Type"),
    path('logout/', views.user_logout, name="Logout")
]
