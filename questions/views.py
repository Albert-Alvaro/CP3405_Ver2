from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'world'
    }
    return render(request, 'index.html', context)