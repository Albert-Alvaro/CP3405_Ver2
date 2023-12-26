from django.shortcuts import render, redirect
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

def shortQuestionPage(request, id):
    short_response_form = ShortResponseForm()
    if request.method == "POST":
        try:
            short_response_form = ShortResponseForm(request.POST)
            if short_response_form.is_valid():
                short_response = short_response_form.save(commit=False)
                short_response.question = ShortQuestion(id=id)
                short_response.save()
        except Exception as e:
            print(e)
            raise

    short_question = ShortQuestion.objects.get(id=id)
    context = {
        'short_question': short_question,
        'short_response_form': short_response_form
    }
    return render(request, 'ShortQuestion.html', context)
def essayQuestionPage(request, id):
    essay_response_form = EssayResponseForm()
    if request.method == "POST":
        try:
            essay_response_form = EssayResponseForm(request.POST)
            if essay_response_form.is_valid():
                essay_response = essay_response_form.save(commit=False)
                essay_response.question = EssayQuestion(id=id)
                essay_response.save()
        except Exception as e:
            print(e)
            raise
    essay_question = EssayQuestion.objects.get(id=id)
    context = {
        'essay_question': essay_question,
        'essay_response_form': essay_response_form
    }
    return render(request, 'EssayQuestion.html', context)
def MCQuestionPage(request, id):
    mcq_question = MultiChoiceQuestion.objects.get(id=id)
    context = {
        'mcq_question': mcq_question
    }
    return render(request, 'MCQ.html', context)