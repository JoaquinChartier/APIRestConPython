from APIRestConPython.functions import *
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse
import json

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        #custom claims
        token['email'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@csrf_exempt
def me(request):
    permission_classes = (IsAuthenticated,)
    res = get_data_from_header(request.META['HTTP_AUTHORIZATION'])
    return JsonResponse(res)

@csrf_exempt
def get_links(request):
    permission_classes = (IsAuthenticated,)
    body = json.loads(request.body)
    html = get_html(body['url'])
    exported_list = scrape_html(html)
    try:
        return route(exported_list, body['output'])
    except UnicodeDecodeError:
        return JsonResponse({"error":"an error ocurred: UnicodeDecodeError"})
    except:
        return JsonResponse({"error":"an unexpected error ocurred"})