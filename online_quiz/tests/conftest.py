import pytest
from pytest_factoryboy import register
from factories import QuizFactory, ContestantFactory
from django.contrib.auth.models import User

register(QuizFactory)
register(ContestantFactory)


@pytest.fixture
def create_quiz(db, quiz_factory):
    quiz = quiz_factory.create()
    return quiz


@pytest.fixture
def create_contestant(db, contestant_factory):
    test_user = User.objects.create_user('Test_user', 'Test_user@gmail.com', 'test_password')
    contestant = contestant_factory.create(user=test_user)
    return contestant
