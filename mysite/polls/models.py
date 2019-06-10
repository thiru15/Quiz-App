from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    correct=models.IntegerField(default=0)

    def __str__(self):
        return str(self.question_text)+"   "+str(self.correct)
    #def __str__(self):
        #return self.correct


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    answer= models.CharField(max_length=200)
    #def ans(self):
    #    return(str(self.answer))
    def __repr__(self):
       return ((self.votes))

class Correct(models.Model):
    answer=models.CharField(max_length=100)
    no_of_correct=models.IntegerField()

    def __str__(self):
        return(self.answer)
