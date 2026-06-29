from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer

from rest_framework.permissions import IsAuthenticated


class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "name": request.user.name,
            "email": request.user.email,
            "plan": request.user.current_plan.name
        })
class SignupView(APIView):

    def post(self, request):

        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "User Registered Successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )




class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(
                request,
                username=email,
                password=password
            )

            if user is None:
                return Response(
                    {"error": "Invalid Email or Password"},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login Successful"
            })

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)



class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "name": request.user.name,
            "email": request.user.email,
            "plan": request.user.current_plan.name
        })
    
class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({
            "message": f"Welcome {request.user.name}",
            "plan": request.user.current_plan.name
        })
from .permissions import IsPremium


class PremiumContentView(APIView):

    permission_classes = [IsAuthenticated, IsPremium]

    def get(self, request):

        return Response({
            "message": "Welcome Premium User!",
            "content": "This is Premium Content."
        })