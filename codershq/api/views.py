import json

from django.contrib.auth import get_user_model
from django.core import serializers
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from codershq.api.utils.analytics import Analytics
from codershq.api.utils.pluralsight import PluralSight
from codershq.portfolio.models import Portfolio
from codershq.users.models import User

from .serializers import RegisterSerializer

User = get_user_model()


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        "users/all/",
        "assessment/skills/all/",
        "users/skills/<int:id>/",
        "assessment/analytics/",
    ]
    return Response(routes)


# -----------------------------------------------------------------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# -----------------------------------------------------------------
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAdminUser])
def users_all(request):
    """
    return all users with pluralsight data
    """
    all_users = Portfolio.objects.all()
    serialized_obj = serializers.serialize('json', all_users)

    data = {"data": json.loads(serialized_obj)}
    return JsonResponse(data, safe=True)


@api_view(['GET'])
def skills_all(requests):
    """
    return all pluralsight skills taken as a json list
    """
    data = {"data": PluralSight.all_skills()}
    return JsonResponse(data, safe=True)


@api_view(['GET'])
def user_id_skills(requests, id):
    """
    return specific user skills based on id
    """

    data = {"data": PluralSight.get_user_skill(id)}
    return JsonResponse(data, safe=True)


@api_view(['GET'])
def analytics_public(requests):
    """
    return important analytics
    """

    analytics = Analytics().json()
    data = {"data": analytics}
    return JsonResponse(data, safe=True)


@api_view(['GET'])
def analytics_private(requests):
    """
    return private analytics
    """
    pass


@api_view(['GET'])
def leaderboard(requests):
    """
    return top users based on skills
    """
    pass
