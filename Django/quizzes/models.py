from django.db import models
from django.conf import settings

class Quiz(models.Model):
    question = models.TextField()
    answers = models.JSONField()
    correct = models.CharField(max_length=2)
    explanations = models.TextField()

class QuizRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date_answered = models.DateField(auto_now_add=True)