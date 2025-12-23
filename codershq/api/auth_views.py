from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LegacyTokenObtainView(APIView):
    """Backwards-compatible JWT endpoint.

    Historically this project exposed `/api-token-auth/` (drf-jwt) which returned
    `{"token": "..."}`. SimpleJWT returns `{access, refresh}`.

    This view preserves the legacy response shape while also returning the
    modern fields.
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data
        access = tokens.get("access")
        refresh = tokens.get("refresh")
        return Response({"token": access, "access": access, "refresh": refresh})
