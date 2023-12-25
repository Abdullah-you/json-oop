from django.test import TestCase
import datetime
from django.utils import timezone
from polls.models import Question

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        time = timezone.now() + datetime.timezone(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
