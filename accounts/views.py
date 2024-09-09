from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSignupSerializer
from django.shortcuts import get_object_or_404

@api_view(["POST"])
def account_signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def account_profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer=UserSignupSerializer(user)
    return Response (serializer.data)


