from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

import glob
import os
import csv


class PopulateData(models.Model):
    data_file = models.FileField(upload_to='files/questions/', max_length=254)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        all_files = glob.glob("media/files/questions/*")
        latest_file = max(all_files, key=os.path.getctime)
        with open(latest_file, 'r') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                ques = Question.objects.create(question_text=row[0])
                for i in range(4):
                    Choice.objects.create(
                        ques=ques, choice_text=row[i+1], isCorrectChoice=(i+1 == int(row[5])))


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100, blank=False)
    isCorrectChoice = models.BooleanField(default=False)

    def __str__(self):
        return self.ques.question_text + '_' + self.choice_text


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    created_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    total_time = models.IntegerField(default=90)
    score = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + '_' + str(self.created_date)


class TestResponses(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE,)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.test.created_date) + '_' + str(self.question.question_text)
