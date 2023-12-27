from django import forms
from .models import *
class AddShortQuestion(forms.ModelForm):
    class Meta:
        model = ShortQuestion
        fields = ['question']

class AddEssayQuestion(forms.ModelForm):
    class Meta:
        model = EssayQuestion
        fields = ['question', 'image']

class AddMCQuestion(forms.ModelForm):
    class Meta:
        model = MultiChoiceQuestion
        fields = ['question']

class AddChoices(forms.ModelForm):
    class Meta:
        model = Choices
        fields = ['choice']

class CreateCategory(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category']

class ShortResponseForm(forms.ModelForm):
    class Meta:
        model = ShortResponse
        fields = ['body']

class EssayResponseForm(forms.ModelForm):
    class Meta:
        model = EssayResponse
        fields = ['body']