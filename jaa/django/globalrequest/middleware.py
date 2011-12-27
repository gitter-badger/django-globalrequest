from context import *

class GlobalRequestMiddleware(object):
    def process_request(self, request):
        set_request(request)
