from django.test import TestCase
from django.contrib.auth.models import User

from quiz.models import Contestant, Profile, Quiz, Question, SubmittedAnswer, QuizCompletion


class TestContestantModel(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('Test_user', 'Test_user@gmail.com', 'test_password')
        self.test_contestant = Contestant.objects.create(user=self.test_user, points=10, is_admin=False)

    def test_contestant_model_entry(self):
        entry = self.test_contestant
        self.assertTrue(isinstance(entry, Contestant))
        self.assertEqual(str(entry.user.email), 'Test_user@gmail.com')
        self.assertEqual(entry.is_admin, False)
        self.assertEqual(int(entry.points), 10)


class TestProfileModel(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('Test_user', 'Test_user@gmail.com', 'test_password')
        self.test_contestant = Contestant.objects.create(user=self.test_user, points=10, is_admin=False)
        self.test_profile = Profile.objects.create(contestant=self.test_contestant, bio='No bio',
                                                   social_link='github.com')

    def test_profile_model_entry(self):
        entry = self.test_profile
        self.assertTrue(isinstance(entry, Profile))
        self.assertEqual(int(entry.contestant.points), 10)
        self.assertEqual(str(entry.bio), 'No bio')
        self.assertEqual(str(entry.social_link), 'github.com')


class TestQuizModel(TestCase):
    def setUp(self):
        self.test_quiz = Quiz.objects.create(title='test_quiz', description='Just testing',
                                             is_public=True)

    def test_quiz_model_entry(self):
        entry = self.test_quiz
        self.assertTrue(isinstance(entry, Quiz))
        self.assertEqual(str(entry), 'test_quiz')
        self.assertEqual(str(entry.description), 'Just testing')
        self.assertEqual(entry.is_public, True)


class TestQuestionModel(TestCase):
    def setUp(self):
        self.test_quiz = Quiz.objects.create(title='test_quiz')
        self.test_question = Question.objects.create(quiz=self.test_quiz, title='test_question',
                                                     answer_1='Answer 1', answer_2='Answer 2',
                                                     answer_3='Answer 3', answer_4='Answer 4',
                                                     right_answer='Right answer', time_limit=60)

    def test_question_model_entry(self):
        entry = self.test_question
        self.assertTrue(isinstance(entry, Question))
        self.assertEqual(str(entry), 'test_question')
        self.assertEqual(str(entry.quiz.title), 'test_quiz')
        self.assertEqual(str(entry.answer_1), 'Answer 1')
        self.assertEqual(str(entry.answer_2), 'Answer 2')
        self.assertEqual(str(entry.answer_3), 'Answer 3')
        self.assertEqual(str(entry.answer_4), 'Answer 4')
        self.assertEqual(str(entry.right_answer), 'Right answer')
        self.assertEqual(int(entry.time_limit), 60)


class TestSubmittedAnswerModel(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('Test_user', 'Test_user@gmail.com', 'test_password')
        self.test_quiz = Quiz.objects.create(title='test_quiz')
        self.test_question = Question.objects.create(quiz=self.test_quiz, title='test_question',
                                                     answer_1='Answer 1', answer_2='Answer 2',
                                                     answer_3='Answer 3', answer_4='Answer 4',
                                                     right_answer='Right answer', time_limit=60)
        self.test_submitted_answer = SubmittedAnswer.objects.create(question=self.test_question,
                                                                    user=self.test_user, chosen_answer='My Answer')

    def test_submitted_answer_model_entry(self):
        entry = self.test_submitted_answer
        self.assertTrue(isinstance(entry, SubmittedAnswer))
        self.assertEqual(str(entry.question.title), 'test_question')
        self.assertEqual(str(entry.user.username), 'Test_user')
        self.assertEqual(str(entry.chosen_answer), 'My Answer')


class TestQuizCompletionModel(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('Test_user', 'Test_user@gmail.com', 'test_password')
        self.test_contestant = Contestant.objects.create(user=self.test_user, points=10, is_admin=False)
        self.test_quiz = Quiz.objects.create(title='test_quiz')
        self.test_quiz_completion = QuizCompletion.objects.create(contestant=self.test_contestant,
                                                                  quiz=self.test_quiz, score=50)

    def test_quiz_completion_model_entry(self):
        entry = self.test_quiz_completion
        self.assertTrue(isinstance(entry, QuizCompletion))
        self.assertEqual(str(entry.quiz.title), 'test_quiz')
        self.assertEqual(int(entry.contestant.points), 10)
        self.assertEqual(int(entry.score), 50)
