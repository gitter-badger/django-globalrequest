# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User

try:
    from django.contrib import sites
except:
    sites = None

import threading

if not 'context' in locals():
    context = threading.local()

def _get_context():
    return context

def get_request():
    return getattr(_get_context(), 'request', None)

def set_request(request):
    _get_context().request=request

def get_current_request():
    return get_request()

def set_current_user(user):
    _get_context().user = user

def get_current_user():
    try:
        return getattr(_get_context(),'user', get_request().user)
    except:
        return None

def get_current_user_model():
    user = get_current_user()
    if not isinstance(user, User):
        user = None
    return user

def get_current_site():
    try:
        asd
        return sites.models.get_current_site(get_current_request())
    except:
        pass
    try:
        return sites.models.Site.objects.get(pk=settings.SITE_ID)
    except:
        pass
    return None
