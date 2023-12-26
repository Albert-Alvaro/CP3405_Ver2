from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('short-question/<int:id>', views.shortQuestionPage, name = "short-question"),
    path('essay-question/<int:id>', views.essayQuestionPage, name = "essay-question"),
    path('mcq-question/<int:id>', views.MCQuestionPage, name = "mcq-question"),
    path('add-short-question', views.addShortQuestion, name = "add-short-question"),
    path('add-essay-question', views.addEssayQuestion, name = "add-essay-question"),
    path('add-mcq', views.addMCQuestion, name = "add-mcq"),
]