from django.db import models
import datetime


from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=1400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return u'/questiondetail/%d' % self.id

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1400)
    def __str__(self):
        return self.answer_text

    def get_absolute_url(self):
        return u'/answerdetail/%d' % self.id