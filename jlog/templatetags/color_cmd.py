# coding=utf-8
from django import template
from django.utils.safestring import mark_safe
from jumpserver.settings import NORMAL_CMD, WARN_CMD, DANGER_CMD

register = template.Library()


@register.filter()
def color_cmd(value):
    try:
        cmd = value.split()[0]
        if NORMAL_CMD.find(cmd) !=-1:
            return mark_safe("<span style='color:#1ab394'>%s</span>" % value)
        if WARN_CMD.find(cmd) !=-1:
            return mark_safe("<span style='color:#f8ac59'>%s</span>" % value)
        if DANGER_CMD.find(cmd) != -1:
            return mark_safe("<span style='color:#ed5565'>%s</span>" % value)
        return value
    except Exception, e:
        return value
