import factory
from quiz.models import Quiz, Contestant
from faker import Faker

fake = Faker()


class QuizFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quiz

    title = "Test Quiz"


class ContestantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contestant

    points = 100
    is_admin = True
