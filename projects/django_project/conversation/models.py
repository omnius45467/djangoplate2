from django.db import models
import datetime


from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=1400)

    def get_absolute_url(self):
        return u'/questiondetail/%d' % self.id

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1400)

    def get_absolute_url(self):
        return u'/answerdetail/%d' % self.id