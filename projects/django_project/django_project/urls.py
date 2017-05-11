"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from django.template import Context, Template
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from conversation.views import ChatterBotAppView, FormCreateView

from conversation import views
from .worker import QuestionCrudManager, AnswerCrudManager


question_crud = QuestionCrudManager()
answer_crud = AnswerCrudManager()

urlpatterns = [
    url(r'^chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot')),
    url(r'^admin/', admin.site.urls),
    # url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^$', FormCreateView, name='form'),
]

urlpatterns += question_crud.get_url_patterns()
urlpatterns += answer_crud.get_url_patterns()

