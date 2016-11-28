# coding:utf-8
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from jumpserver.api import *
from jperm.perm_api import user_have_perm
from django.http import HttpResponseNotFound
from jlog.log_api import renderJSON

from jlog.models import Log, ExecLog, FileLog, TermLog, RunProcess, HadoopProcess
from jumpserver.settings import LOG_DIR
import zipfile
import json
import pyte


@require_role('admin')
def log_alarm(request, offset):
    header_title, path1 = u'告警', u'告警查询'

    posts = ExecLog.objects.all().order_by('-id')
    keyword = request.GET.get('keyword', '')
    query_cmd = []
    if offset == "normal":
        query_cmd = filter(lambda item: item.strip() != "", NORMAL_CMD.split(","))
    if offset == "warn":
        query_cmd = filter(lambda item: item.strip() != "", WARN_CMD.split(","))
    if offset == "danger":
        query_cmd = filter(lambda item: item.strip() != "", DANGER_CMD.split(","))
    where = None
    for cmd in query_cmd:
        if not query_cmd:
            continue
        if where is None:
            where = Q(cmd__icontains=cmd.strip())
        else:
            where |= Q(cmd__icontains=cmd.strip())
    if keyword:
        if where is None:
            where = (Q(user__icontains=keyword) | Q(host__icontains=keyword) | Q(cmd__icontains=keyword))
        else:
            where &= (Q(user__icontains=keyword) | Q(host__icontains=keyword) | Q(cmd__icontains=keyword))
    if where:
        posts = posts.filter(where)
    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
    session_id = request.session.session_key
    return render_to_response('jalarm/log_alarm.html', locals(), context_instance=RequestContext(request))
