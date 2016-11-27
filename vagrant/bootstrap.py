# coding=utf-8
import os

import sys

import django

jms_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(jms_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'jumpserver.settings'
if django.get_version() != '1.6':
    setup = django.setup()

from juser.user_api import db_add_user, get_object, User
from jumpserver.api import get_mac_address, bash

db_add_user(username="admin", password="admin123", role='SU', name='admin', groups='', admin_groups='',
            email='admin@jumpserver.org', uuid='MayBeYouAreTheFirstUser', is_active=True)
