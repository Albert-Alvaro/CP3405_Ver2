from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('create-category', views.createCategory, name="create-category"),
    path('create-category-add-question/<int:id>', views.addQuestionToCategory, name="create-category-add-question"),
    path('add-essay-question-to-category/<int:id>/<int:id2>', views.addEssayQuestionToCategory,name="add-essay-question-to-category"),
    path('add-short-question-to-category/<int:id>/<int:id2>', views.addShortQuestionToCategory,
         name="add-short-question-to-category"),
    path('add-mcq-to-category/<int:id>/<int:id2>', views.addMCQToCategory, name="add-mcq-to-category"),
    path('image_upload', views.addEssayQuestion, name='image_upload'),
    path('change-short-question-cat/<int:id>/<int:id2>', views.changeShortQuestionCat, name='change-short-question-cat'),
    path('change-essay-question-cat/<int:id>/<int:id2>', views.changeEssayQuestionCat, name='change-essay-question-cat'),
    path('change-mcq-cat/<int:id>/<int:id2>', views.changeMCQCat, name='change-mcq-cat'),
    path('category-page', views.categoryPage, name="category-page"),
    path('delete-category/<int:id>', views.deleteCategory, name="delete-category"),
    path('category-popup/<int:id>', views.categoryPopup, name="category-popup"),
]
