import threading

if not 'context' in locals():
    context = threading.local()

def get_request():
    return getattr(context, 'request', None)

def set_request(request):
    context.request=request
