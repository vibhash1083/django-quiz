from django.db import models
from django.utils import timezone
import datetime
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
                for data in row:
                    ques = Question.objects.create(question_text=row[0])
                    for i in range(4):
                        Choice.objects.create(
                            ques=ques, choice_text=row[i+1])


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.ques.question_text + '_' + self.choice_text
