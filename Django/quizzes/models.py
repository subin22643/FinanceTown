from django.db import models

class Quiz(models.Model):
    question = models.TextField()
    answers = models.JSONField()
    correct = models.CharField(max_length=1)