import threading

if not 'context' in locals():
    context = threading.local()

def get_request():
    return getattr(context, 'request', None)

def set_request(request):
    context.request=request

def get_current_request():
    return get_request()

def get_current_user():
    try:
        return get_request().user
    except:
        return None
