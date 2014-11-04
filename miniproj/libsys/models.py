from django.db import models
import datetime
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Member(models.Model):
	mid = models.AutoField(primary_key = True)
	bday = models.DateTimeField()
	fname = models.CharField(max_length = 50)
	midname = models.CharField(max_length = 50)
	lname = models.CharField(max_length = 50)
	password = models.CharField(max_length = 100, default="")
	address = models.CharField(max_length = 50)
	phone = models.IntegerField()
	age = models.IntegerField()
	occupation = models.CharField(max_length = 50)
	def __unicode__(self):
		return self.fname

class Publisher(models.Model):
	pid = models.CharField(max_length = 200, primary_key = True)
	name = models.CharField(max_length = 200)
	paddress = models.CharField(max_length = 200)
	pphone = models.IntegerField(max_length = 10)
	def __unicode__(self):
		return self.pid

class Section(models.Model):
	sid = models.CharField(max_length = 200, primary_key = True)
	sname = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.sname

class Book(models.Model):
	bid = models.CharField(max_length = 200, primary_key = True)
	title = models.CharField(max_length = 200)
	price = models.IntegerField(max_length = 20)
	noofcopies = models.IntegerField(max_length = 20, default=0)
	author = models.CharField(max_length = 200)
	pubid = models.ForeignKey(Publisher)
	secid = models.ForeignKey(Section)
	def __unicode__(self):
		return self.bid
 
class Borrow(models.Model):
	bookid = models.ForeignKey(Book)
 	memid = models.ForeignKey(Member)
 	issuedate = models.DateField()
 	duedate = models.DateField()


class SignupForm(ModelForm):
	class Meta:
		model = Member
		exclude = []
