from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from quiz.models import Question


def home(request):
    return render(request, 'quiz/home.html')

def quiz(request):
    obj = Question.objects.all()
    paginator = Paginator(obj, 1)

    page = int(request.GET.get('page', '1'))
    questions = paginator.page(page)

    return render(request, 'quiz/quiz.html',
                  { 'obj' : obj, 'questions' : questions, })

lst=[]
answers = Question.objects.all()
anslist = []

for i in answers:
    anslist.append(i.answer)

def result(request):
    score = 0
    for i in range(len(lst)):
        score += 1

    return render(request, 'quiz/result.html',
                  {'score' : score, 'lst' : lst, 'anslist' : anslist})

def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)