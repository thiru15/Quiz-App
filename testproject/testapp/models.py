from django.db import models

# Create your models here.
class Users(models.Model):
    user = models.CharField(max_length=100,primary_key=True)
    email=models.CharField(max_length=100)
    #password = models.CharField(max_length=100)
    scores = models.IntegerField(default=0)

    def __str__(self):
        return(str(user)+" "+str(self.scores))

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
