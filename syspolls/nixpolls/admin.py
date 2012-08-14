__author__ = 'rost'
from syspolls.nixpolls.models import Group, Quest, UserAnswer, Version
from django.contrib import admin

class GroupAdmin(admin.ModelAdmin):
    model = Group

class QuestAdmin(admin.ModelAdmin):
    model = Quest
    list_filter = ['groups']
    search_fields = ['title_quest']
    list_display = ('groups', 'title_quest',)

class UserAnswerAdmin(admin.ModelAdmin):
    model = UserAnswer

class VersionAdmin(admin.ModelAdmin):
    model = Version

admin.site.register(Quest, QuestAdmin)
admin.site.register(Group)
admin.site.register(UserAnswer)
admin.site.register(Version)
