from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from quiz.models import Question, UserAnswer

lst=[]

def home(request):
    if request.GET:
        user = UserAnswer()
        user.name = request.GET['name']
        if request.GET['name'] == "":
            user.name = "익명"
        user.save()
        return redirect("quiz", user.pk)

    return render(request, 'quiz/home.html')

def quiz(request,pk):
    # obj = Question.objects.all()
    # paginator = Paginator(obj, 1)
    #
    # page = int(request.GET.get('page', '1'))
    # questions = paginator.page(page)
    #
    # return render(request, 'quiz/quiz.html',
    #               { 'obj' : obj, 'questions' : questions, })
    user = get_object_or_404(UserAnswer, pk=pk)


    if request.POST:
        num = int(request.POST['quiz_id']) + 1
        #user.answer =

answers = Question.objects.all()
anslist = []

for i in answers:
    anslist.append(i.answer)

def result(request):
    score = 0
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score += 1

    return render(request, 'quiz/result.html',
                  {'score' : score, 'lst' : lst, 'anslist' : anslist})

def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)