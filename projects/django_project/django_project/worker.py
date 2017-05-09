from generic_scaffold import CrudManager
from conversation.models import Question
from conversation.models import Answer

class QuestionCrudManager(CrudManager):
    model = Question
    prefix = 'question'

class AnswerCrudManager(CrudManager):
    model = Answer
    prefix = 'answer'

