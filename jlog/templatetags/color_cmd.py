# coding=utf-8
from django import template
from django.utils.safestring import mark_safe
from jumpserver.api import DANGER_CMD

register = template.Library()


@register.filter()
def color_cmd(value):
    try:
        cmd = value.split()[0]
        if DANGER_CMD.find(cmd) != -1:
            return mark_safe("<span style='color:red'>%s</span>" % value)
        return value
    except Exception, e:
        return value
