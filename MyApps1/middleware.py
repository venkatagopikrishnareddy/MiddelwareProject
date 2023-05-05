class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        print("init() is executed only once..!!")
        self.get_response = get_response

    def __call__(self, request):
        print('This line added at pre-processing of request')
        response = self.get_response(request)
        print('This line added at post-processing of request')
        return response

#2-Example
from django.http import HttpResponse
class AppMaintananceMiddleware(object):
    def __init__(self, get_response):
        print("init() method is called...");
        self.get_response = get_response

    def __call__(self, request):
        return HttpResponse('<h1>Currently Application under maintenance...Plz try after 8am..!!</h1><hr />')

#3-example
from django.http import HttpResponse


class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        print("init() is called for error-app");
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    '''
    def process_exception(self, request, exception):
        print("Server is printing exception")
        return HttpResponse(
            '<h1> Currently we are facing some technical problems..(Exception) Plz try after some time !!!</h1><hr />')
'''
    def process_exception(self, request, exception):
        print("Server is printing exception")
        return HttpResponse(
         '<h1> Currently we are facing some technical problems..(Exception) plz try after some time !!!</h1><hr /><h2>Raised Exception:{}</h2><h3>Exception Message : {}</h3>'.format(
            exception.__class__.__name__, exception));

#finall-example
class FirstMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('This line printed by FirstMiddleware at pre-processing of request');
        response = self.get_response(request)
        print('This line printed by FirstMiddleware at post-processing of request')
        return response;

class SecondMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('This line printed by SecondMiddleware at pre-processing of request')
        response = self.get_response(request)
        print('This line printed by SecondMiddleware at post-processing of request')
        return response

