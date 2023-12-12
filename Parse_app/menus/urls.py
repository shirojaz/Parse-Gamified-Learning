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
    path('logout/', views.user_logout, name="Logout"),

#10 Question Batch
    path('python/Quiz/1', views.question1, name='Question 1'),
    path('python/Quiz/1-ans', views.question1_ans, name='Question 1 Answer'),

    path('python/Quiz/2', views.question2, name='Question 2'),
    path('python/Quiz/2-ans', views.question2_ans, name='Question 2 Answer'),

    path('python/Quiz/3', views.question3, name='Question 3'),
    path('python/Quiz/3-ans', views.question3_ans, name='Question 3 Answer'),

    path('python/Quiz/4', views.question4, name='Question 4'),
    path('python/Quiz/4-ans', views.question4_ans, name='Question 4 Answer'),

    path('python/Quiz/5', views.question5, name='Question 5'),
    path('python/Quiz/5-ans', views.question5_ans, name='Question 5 Answer'),

    path('python/Quiz/6', views.question6, name='Question 6'),
    path('python/Quiz/6-ans', views.question6_ans, name='Question 6 Answer'),

    path('python/Quiz/7', views.question7, name='Question 7'),
    path('python/Quiz/7-ans', views.question7_ans, name='Question 7 Answer'),

    path('python/Quiz/8', views.question8, name='Question 8'),
    path('python/Quiz/8-ans', views.question8_ans, name='Question 8 Answer'),

    path('python/Quiz/9', views.question9, name='Question 9'),
    path('python/Quiz/9-ans', views.question9_ans, name='Question 9 Answer'),

    path('python/Quiz/10', views.question10, name='Question 10'),
    path('python/Quiz/10-ans', views.question10_ans, name='Question 10 Answer'),

    path("python/Quiz/Woohoo!", views.congrats, name="Congratulations")
]
