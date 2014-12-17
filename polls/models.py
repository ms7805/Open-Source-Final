import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True, default=None)
    picture = models.ImageField(upload_to='profile_pic', blank = True)
    def __unicode__(self):
        return self.user.username

class Question(models.Model):
    question_title = models.CharField(max_length=100, default="No Topic")
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published',default=timezone.now(),blank=True)
    modified_date = models.DateTimeField('date modified',default=timezone.now(),blank=True)
    user = models.ForeignKey(UserProfile,null=True)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, blank=True)
    choice_title = models.CharField(max_length=50,default="No Title")
    choice_text = models.CharField(max_length=200)
    creator = models.ForeignKey(UserProfile,null=True)
    votes = models.IntegerField(default=0)
    ans_date = models.DateTimeField('date published',default=timezone.now(),blank=True)
    modified_date = models.DateTimeField('date modified',default=timezone.now(),blank=True)
    def __unicode__(self):
        return self.choice_text