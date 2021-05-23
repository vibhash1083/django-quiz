from celery.decorators import task
from quiz.models import *


@task
def calculate_score(test_id):
    test = Test.objects.get(id=test_id)
    test_responses = TestResponses.objects.filter(test=test)
    score = 0
    for response in test_responses:
        if response.choice.isCorrectChoice:
            score += 1
    print(score)
    test.score = score
    test.save()
