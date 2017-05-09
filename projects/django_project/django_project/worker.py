from generic_scaffold import CrudManager
from conversation.models import Question

class QuestionCrudManager(CrudManager):
    model = Question
    prefix = 'question'