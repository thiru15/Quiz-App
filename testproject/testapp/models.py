from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models

 



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)

    def __str__(self):
        return(str(self.user)+" has scored "+str(self.scores)+" marks")
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    correct=models.CharField(max_length=150)

    def __str__(self):
        return str(self.question_text)+"   "+str(self.correct)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #answer= models.CharField(max_length=200)
    #def ans(self):
    #    return(str(self.answer))
    def __repr__(self):
       return ((self.votes))
