
from __future__ import print_function
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from conversation.models import Question
from conversation.models import Answer
from django.views.generic.base import TemplateView

from .forms import NewQuestionForm

import psutil
# 
# 
class ChatterBotAppView(TemplateView):
    template_name = "conversation/index.html"
# def home(request):
#     context_data = Question.objects.all()
#     return render(request, 'conversation/index.html', {'context_data': context_data})


def FormCreateView(request):
    context_data = Question.objects.all()
    recent_question = Question.objects.latest('question_text')

    system_data_1 = psutil.cpu_percent()
    system_data_2 = psutil.virtual_memory()
    # question_inst = get_object_or_404(recent_question)
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            # recent_question.question_text = form.cleaned_data['question_text']
            q = Question(question_text=form.cleaned_data['question_text'])
            q.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        
        form = NewQuestionForm(initial={'question_text': '', })

    return render(request, 'conversation/index.html', {'form': form, 'question_inst': recent_question, 'context_data': context_data, 'system_data_1': system_data_1, 'system_data_2': system_data_2})