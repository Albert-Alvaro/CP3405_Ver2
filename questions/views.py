from django.shortcuts import render
from .models import *

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

def questionPage(request, id):
    return None