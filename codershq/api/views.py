from django.core import serializers
from django.http import JsonResponse

from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .serializers import MyTokenObtainPairSerializer,SSOSerializer,RegisterSerializer
from rest_framework.permissions import AllowAny
from djangosaml2idp.models import ServiceProvider
from django.urls import reverse
from codershq.events.models import Event
# from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from codershq.users.models import User

User=get_user_model() 


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh',
        # reverse('saml_idp_init',kwargs = {'sp': 'tttt' }),
        'http://localhost:8000/idp/sso/init?sp=IAMShowcase',
    ]
    return Response(routes)


#-----------------------------------------------------------------
#User Authentication:
#https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html



class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


#-----------------------------------------------------------------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

#-------------------------------------------------------------
#SSO

class SSOView(generics.CreateAPIView):
    queryset = ServiceProvider.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SSOSerializer


#-----------------------------------------------------------------
#Events

def events(request):
    events = Event.objects.all()
    data = serializers.serialize(
        "json",
        events,
        fields=[
            "title",
            "short_description",
            "date_time",
            "location",
            "image",
            "duration",
            "event_link",
        ],
    )

    return JsonResponse(data, safe=False)