from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse
from syspolls.nixpolls.models import Quest, UserAnswer, Group, Version
from django.contrib.auth.decorators import login_required

import logging

@login_required
def groups(request):
    groups_v = Group.objects.all()
    version_v = Version.objects.all()
    ctx = {
        'groups_v':groups_v, 'version_v':version_v,
    }
    return render_to_response('groups.html', RequestContext(request, ctx))

@login_required
def quests(request, title):
    group_s = get_object_or_404(Group, title__iexact=title)
    quests_v = Quest.objects.filter(groups=group_s).order_by('groups')
    if request.method == 'POST':
        for q in quests_v:
            t = 'qust_%s' % q.id
            t2 = 'ans_%s' % q.id
            qst_db = request.POST.get(t, '')
            qst_db_an = request.POST.get(t2, '')
            answer_obj = UserAnswer(user_name=request.user, group=group_s, quest=qst_db, answer=qst_db_an)
            answer_obj.save()
    ctx = {
        'quests_v':quests_v,
    }
    return render_to_response('polls.html', RequestContext(request, ctx))