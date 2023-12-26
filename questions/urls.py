from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('question/<int:id>', views.questionPage, name = "question"),
    path('add-short-question', views.addShortQuestion, name = "add-short-question"),
    path('add-essay-question', views.addEssayQuestion, name = "add-essay-question"),
    path('add-mcq', views.addMCQuestion, name = "add-mcq"),
]