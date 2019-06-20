from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)

    def __str__(self):
        return(str(self.user)+" has scored "+str(self.scores)+" marks")

class Quiz1(models.Model):
    question_text = models.CharField(max_length=100)
     
    correct= models.CharField(max_length=200)

    def __str__(self):
        return str(self.question_text)+" "+str(self.correct)

class Choice(models.Model):
    question = models.ForeignKey(Quiz1, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __repr__(self):
       return ((self.votes))

class Quiz2(models.Model):
    question_text = models.CharField(max_length=100)
     
    correct= models.CharField(max_length=200)

    def __str__(self):
        return str(self.question_text)+" "+str(self.correct)
class Choice2(models.Model):
    question = models.ForeignKey(Quiz2, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __repr__(self):
       return ((self.votes))
class Profile1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)

    def __str__(self):
        return(str(self.user)+" has scored "+str(self.scores)+" marks in quiz1")

class Profile2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)

    def __str__(self):
        return(str(self.user)+" has scored "+str(self.scores)+" marks in quiz1")



