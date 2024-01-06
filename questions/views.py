import random

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
                return redirect("/")
        except Exception as e:
            print(e)
            raise
    context = {'form': form}
    return render(request, 'add_short_question.html', context)

def addEssayQuestion(request):
    form = AddEssayQuestion()
    if request.method == "POST":
        try:
            form = AddEssayQuestion(request.POST, request.FILES)
            if form.is_valid():
                question = form.save(commit=False)
                question.save()
                return redirect("/")
        except Exception as e:
            print(e)
            raise
    context = {'form': form}
    return render(request, 'add_essay_question.html', context)

def addMCQuestion(request):
    form = AddMCQuestion()
    if request.method == "POST":
        try:
            form = AddMCQuestion(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.save()
                return redirect('/add_mcq_add_choice/'+str(question.id))
        except Exception as e:
            print(e)
            raise
    context = {
        'form': form,
    }
    return render(request, 'add_mcq.html', context)

def addChoice(request, id):
    choices = Choices.objects.filter(mcq=id)
    multiChoiceQuestions = MultiChoiceQuestion.objects.get(id=id)
    print(choices)
    form = AddChoices()
    if request.method == "POST":
        form = AddChoices(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.mcq = MultiChoiceQuestion(id=id)
            choice.save()
            form = AddChoices()
            return redirect("/add_mcq_add_choice/"+str(id))
    context = {
        'form': form,
        'multiChoiceQuestions': multiChoiceQuestions,
        'choices': choices
    }
    print(choices)
    return render(request, 'add_mcq_add_choice.html', context)

def shortQuestionPage(request, id):
    category = Question.objects.all()
    short_response_form = ShortResponseForm()
    if request == "POST":
        try:
            short_response_form = ShortResponseForm(request.POST)
            if short_response_form.is_valid():
                short_response = short_response_form.save(commit=False)
                short_response.question = ShortQuestion(id=id)
                short_response.save()
                return redirect("/")
        except Exception as e:
            print(e)
            raise
    short_question = ShortQuestion.objects.get(id=id)
    context = {
        'short_question': short_question,
        'short_response_form': short_response_form,
        'category': category
    }
    return render(request, 'ShortQuestion.html', context)

def deleteShortQuestion(request, id):
    short_question = ShortQuestion.objects.filter(id=id)
    short_question.delete()
    return redirect("/")
def deleteEssayQuestion(request, id):
    essay_question = EssayQuestion.objects.filter(id=id)
    essay_question.delete()
    return redirect("/")
def deleteChoice(request, id):
    choice = Choices.objects.get(id=id)
    choice.delete()
    return redirect("/mcq-question/"+str(choice.mcq.id))
def deleteMCQ(request, id):
    mcq_question = MultiChoiceQuestion.objects.filter(id=id)
    choice = Choices.objects.filter(id=id)
    mcq_question.delete()
    choice.delete()
    return redirect("/")
def deleteChoice_amcq(request, id):
    choice = Choices.objects.get(id=id)
    choice.delete()
    return redirect("/add_mcq_add_choice/"+str(choice.mcq.id))

def essayQuestionPage(request, id):
    category = Question.objects.all()
    essay_response_form = EssayResponseForm()
    question = EssayQuestion.objects.get(id=id)
    print(question.image)
    image = question.image
    if request.method == "POST":
        try:
            essay_response_form = EssayResponseForm(request.POST)
            if essay_response_form.is_valid():
                essay_response = essay_response_form.save(commit=False)
                essay_response.question = EssayQuestion(id=id)
                essay_response.save()
                return redirect("/")
        except Exception as e:
            print(e)
            raise
    essay_question = EssayQuestion.objects.get(id=id)
    context = {
        'essay_question': essay_question,
        'essay_response_form': essay_response_form,
        'category': category,
        'image': image
    }
    return render(request, 'EssayQuestion.html', context)
def MCQuestionPage(request, id):
    category = Question.objects.all()
    mcq_question = MultiChoiceQuestion.objects.get(id=id)
    choices = Choices.objects.filter(mcq=id)
    form = AddChoices()
    if request.method == "POST":
        form = AddChoices(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.mcq = MultiChoiceQuestion(id=id)
            choice.save()
            form = AddChoices()
            return redirect("/mcq-question/" + str(id))
    context = {
        'mcq_question': mcq_question,
        'choices': choices,
        'form': form,
        'category': category
    }
    return render(request, 'MCQ.html', context)

def createCategory(request):
    form = CreateCategory()
    if request.method == "POST":
        form = CreateCategory(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            form = CreateCategory()
            return redirect("/create-category-add-question/"+ str(question.id))
    context = {
        'form': form,
    }
    return render(request, 'create_category.html', context)
def addQuestionToCategory(request, id):
    shortQuestions = ShortQuestion.objects.all()
    essayQuestions = EssayQuestion.objects.all()
    multiChoiceQuestions = MultiChoiceQuestion.objects.all()
    shortQuestionsCat = ShortQuestion.objects.filter(category=id)
    essayQuestionsCat = EssayQuestion.objects.filter(category=id)
    multiChoiceQuestionsCat = MultiChoiceQuestion.objects.filter(category=id)
    category = Question.objects.get(id=id)
    print(id)
    print(shortQuestionsCat)
    print(shortQuestions.values_list('category'))
    context = {
        'shortQuestions': shortQuestions,
        'essayQuestions': essayQuestions,
        'multiChoiceQuestions': multiChoiceQuestions,
        'shortQuestionsCat':shortQuestionsCat,
        'essayQuestionsCat':essayQuestionsCat,
        'multiChoiceQuestionsCat': multiChoiceQuestionsCat,
        'category': category,
    }
    return render(request, 'create_category_add_question.html', context)

def addShortQuestionToCategory(request, id, id2):
    category = Question.objects.get(id=id)
    question = ShortQuestion.objects.filter(id=id2).update(category=id)
    return redirect("/create-category-add-question/" + str(category.id))
def addEssayQuestionToCategory(request, id, id2):
    category = Question.objects.get(id=id)
    question = EssayQuestion.objects.filter(id=id2).update(category=id)
    return redirect("/create-category-add-question/" + str(category.id))
def addMCQToCategory(request, id, id2):
    category = Question.objects.get(id=id)
    question = MultiChoiceQuestion.objects.filter(id=id2).update(category=id)

    return redirect("/create-category-add-question/" + str(category.id))

def changeShortQuestionCat(request, id, id2):
    category = Question.objects.get(id=id2)
    short_question = ShortQuestion.objects.filter(id=id).update(category=id2)
    return redirect("/short-question/"+str(id))
def changeEssayQuestionCat(request, id, id2):
    category = Question.objects.get(id=id2)
    essay_question = EssayQuestion.objects.filter(id=id).update(category=id2)
    return redirect("/essay-question/"+str(id))
def changeMCQCat(request, id, id2):
    category = Question.objects.get(id=id2)
    mcq_question = MultiChoiceQuestion.objects.filter(id=id).update(category=id2)

    return redirect("/mcq-question/"+str(id))

def categoryPage(request):
    category = Question.objects.all()
    context= {
        'category': category,
    }
    return render(request, 'Category.html', context)

def deleteCategory(request, id):
    category = Question.objects.get(id=id)
    question = ShortQuestion.objects.filter(category=id).update(category='')
    question2 = EssayQuestion.objects.filter(category=id).update(category='')
    question3 = MultiChoiceQuestion.objects.filter(category=id).update(category='')
    category.delete()
    return redirect("/category-page")

def categoryPopup(request, id):
    category = Question.objects.get(id=id)
    shortQuestionsCat = ShortQuestion.objects.filter(category=id)
    essayQuestionsCat = EssayQuestion.objects.filter(category=id)
    multiChoiceQuestionsCat = MultiChoiceQuestion.objects.filter(category=id)
    context ={
        'shortQuestionsCat': shortQuestionsCat,
        'essayQuestionsCat': essayQuestionsCat,
        'multiChoiceQuestionsCat': multiChoiceQuestionsCat,
        'category': category,
    }
    return render(request, 'CategoryPopup.html', context)

def image(request, id):
    question = EssayQuestion.objects.get(id=id)
    print(question.image)
    image = question.image
    return redirect("/essay-question/"+ int(question.id))
# make second function that add a button in essayquestion page and jump to another url to display picture, then that page just have picture and come back to question.