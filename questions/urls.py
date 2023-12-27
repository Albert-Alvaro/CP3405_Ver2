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
    path('add_mcq_add_choice/<int:id>', views.addChoice, name="add_mcq_add_choice"),
    path('delete-short-question/<int:id>/', views.deleteShortQuestion, name='delete-short-question'),
    path('delete-essay-question/<int:id>/', views.deleteEssayQuestion, name='delete-essay-question'),
    path('delete-mcq/<int:id>/', views.deleteMCQ, name='delete-mcq'),
    path('delete-choice/<int:id>/', views.deleteChoice, name='delete-choice'),
    path('delete-choice-amcq/<int:id>/', views.deleteChoice_amcq, name='delete-choice-amcq'),
]