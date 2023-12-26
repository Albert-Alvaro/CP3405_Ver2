from django import forms
from .models import *
class AddShortQuestion(forms.ModelForm):
    class Meta:
        model = ShortQuestion
        fields = ['question']

class AddEssayQuestion(forms.ModelForm):
    class Meta:
        model = EssayQuestion
        fields = ['question']

class AddMCQuestion(forms.ModelForm):
    class Meta:
        model = MultiChoiceQuestion
        fields = ['question', 'choices']

class AddChoices(forms.ModelForm):
    class Meta:
        model = Choices
        fields = ['choice']

class ShortResponseForm(forms.ModelForm):
    class Meta:
        model = ShortResponse
        fields = ['body']

class EssayResponseForm(forms.ModelForm):
    class Meta:
        model = EssayResponse
        fields = ['body']