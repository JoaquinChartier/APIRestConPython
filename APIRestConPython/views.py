from django.http import HttpResponse
from APIRestConPython.functions import *
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def me(request):
    permission_classes = (IsAuthenticated,)
    res = get_data_from_header(request.META['HTTP_AUTHORIZATION'])
    return HttpResponse(res, content_type='application/json')

def get_links(request):
    return HttpResponse('Get links', content_type='application/json')