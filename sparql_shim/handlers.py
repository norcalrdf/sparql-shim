from pyramid.view import action

class MyHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='mytemplate.mako')
    def index(self):
        return {'project':'sparql_shim'}
