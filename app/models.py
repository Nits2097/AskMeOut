from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils.translation import gettext as _

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

############################################################
#from vote.models import VoteModel

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    word = models.CharField(max_length=80)
    explanation = models.TextField()

    def __str__(self):
        return self.author.first_name

############################################

# Create your models here.
class Question(models.Model):
	name = models.TextField(max_length = 500)
	uid = models.CharField(max_length=500)
	qid=models.IntegerField(primary_key=True)
	boolValue = models.BooleanField(default=False)
	#category = models.CharField(auto_now_add=True)

class User(models.Model):
	name=models.CharField(max_length = 500)
	uid = models.CharField(max_length=500)
	password = models.CharField(max_length=500)

class Answer(VoteModel, models.Model):
	name = models.TextField(max_length = 500)
	uid = models.CharField(max_length = 500)
	quesid=models.IntegerField()
	aid=models.CharField(max_length = 500)
	voting = models.IntegerField()

class call(models.Model):
	callid=models.IntegerField(primary_key=True)
	sentiment=models.CharField(max_length=10)
	summary=models.CharField(max_length=500)
	service_provider=models.CharField(max_length=100)
	intent=models.CharField(max_length=100)
	rating=models.IntegerField()
	ccid=models.IntegerField()
	text=models.TextField(max_length=1000)
	date = models.DateField(_("Date"), default=datetime.date.today)
	time = models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True)


class employee(models.Model):
	eid=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=50)
	total_calls=models.IntegerField()
	total_minutes=models.IntegerField()
	rating=models.IntegerField()
	sentiment=models.CharField(max_length=500)
	salary=models.IntegerField()






