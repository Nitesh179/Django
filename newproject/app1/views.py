from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(['PUT'])
def index(req):
    return HttpResponse("hello django")

def index2(req):
    return HttpResponse("hello django this is normal method")