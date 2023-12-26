from django.shortcuts import render
from .models import *
from .form import *

# Create your views here.
def index(request):
    shortQuestions = ShortQuestion.objects.all().order_by('created_at')
    multiChoiceQuestions = MultiChoiceQuestion.objects.all().order_by('created_at')
    essayQuestions = EssayQuestion.objects.all().order_by('created_at')
    context = {
        'shortQuestions' : shortQuestions,
        'essayQuestions' : essayQuestions,
        'multiChoiceQuestions' : multiChoiceQuestions,
    }
    return render(request, 'index.html', context)

def addShortQuestion(request):
    form = AddShortQuestion()

    if request.method == "POST":
        try:
            form = AddShortQuestion(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.save()
        except Exception as e:
            print(e)
            raise
    context = {'form': form}
    return render(request, 'add_short_question.html', context)

def addEssayQuestion(request):
    form = AddEssayQuestion()
    if request.method == "POST":
        try:
            form = AddEssayQuestion(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.save()
        except Exception as e:
            print(e)
            raise
    context = {'form': form}
    return render(request, 'add_essay_question.html', context)

def addMCQuestion(request):
    form = AddMCQuestion()
    form2 = AddChoices()
    if request.method == "POST":
        try:
            form = AddMCQuestion(request.POST)
            form2 = AddChoices(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                choice = form2.save(commit=False)
                question.save()
                choice.save()
        except Exception as e:
            print(e)
            raise
    context = {
        'form': form,
        'form2': form2,
    }
    return render(request, 'add_mcq.html', context)

def questionPage(request, id):
    return None