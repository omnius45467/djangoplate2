from django import forms
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class NewQuestionForm(forms.Form):
    question_text = forms.CharField(help_text='enter a question here')