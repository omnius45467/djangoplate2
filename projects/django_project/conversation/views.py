from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from conversation.models import Question
from conversation.models import Answer


def home(request):
    context_data = Question.objects.all()
    return render(request, 'conversation/index.html', {'context_data': context_data})

