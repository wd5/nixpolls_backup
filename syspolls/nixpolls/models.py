from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.models import User

class Group(models.Model):
    title = models.CharField(_("Groups"), max_length=100, blank=False, null=False)

    def __unicode__(self):
        return self.title

class Quest(models.Model):
    groups = models.ForeignKey(Group)
    title_quest = models.CharField(_("Question Name"), max_length=255, blank=False, null=False)

    def __unicode__(self):
        return self.title_quest

class UserAnswer(models.Model):
    date_answer = models.DateField(auto_now_add=True)
    user_name = models.CharField(max_length=15, blank=False, null=False,)
    group = models.CharField(max_length=20, blank=False, null=False,)
    quest = models.CharField(max_length=100, blank=False, null=False,)
    answer = models.CharField(max_length=1, blank=False, null=False,)

class Version(models.Model):
    date_change = models.DateField(auto_now_add=True)
    title_version = models.CharField(_("Version of App"), max_length=255, blank=False, null=False)

    def __unicode__(self):
        return self.title_version
