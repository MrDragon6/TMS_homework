def test_quiz(create_quiz):
    assert create_quiz.title == "Test Quiz"


def test_contestant(create_contestant):
    assert create_contestant.points == 100
    assert create_contestant.is_admin is True
