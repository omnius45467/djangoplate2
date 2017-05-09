from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from conversation.models import Question


def home(request):
    context_data = Question.objects.all()
    # list_result = [entry for entry in context_data]
    # t = loader.get_template('conversation/index.html')
    # context = Question.objects.all()
    # template = 'conversation/index.html'
    # return render(request, template, context)
    # return HttpResponse(t.render(context_data))
    return render(request, 'conversation/index.html', {'context_data': context_data})

