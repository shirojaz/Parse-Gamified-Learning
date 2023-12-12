from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .forms import AccountForm, UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *
import random
# Create your views here.



def startpage(request):
    template = loader.get_template('startpage.html')
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def courses(request):
    context = {'categories': Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quizzes/?category={request.GET.get('category')}")
    return render(request, 'Courses.html', context)

def quiz_instance(request):
    context = {'category' : request.GET.get('category')}
    return render(request, 'quiz.html', context)

def quiz_typeB(request):
    template = loader.get_template('quiz_typeb.html')
    return HttpResponse(template.render())

def account(request):
    acc = loader.get_template('account.html')
    return HttpResponse(acc.render())

def successfulAccount(request):
    acc = loader.get_template('account_success.html')
    return render(request, 'account_success.html')

def about(request):
    return render(request, 'about.html')

def error(request):
    return render(request, 'error.html')

def finished(request):
    # Logic for the finished courses page
    return render(request, 'finished.html')

def help(request):
    return render(request, 'help.html')

def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))

        question_objs = list(question_objs)
        data = []

        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()
            })
            
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
        # Return an HttpResponse even in case of exception
        return HttpResponse("Something went wrong", status=500)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username_ = form.cleaned_data.get('username')
            password_ = form.cleaned_data.get('password')
            user = authenticate(username=username_, password=password_)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/dashboard')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = UserRegistrationForm()
    return render(request=request, template_name='signup.html', context={'form':form})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def account(request):
    currentUser = request.user
    return render(request, 'account.html', {'user': currentUser})

def user_logout(request):
    logout(request)
    return redirect('/')
