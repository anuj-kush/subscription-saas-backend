from rest_framework import serializers
from .models import User
from plans.models import Plan


class UserSerializer(serializers.ModelSerializer):

    current_plan = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "current_plan",
            "created_at",
        ]


class SignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
        ]

    def create(self, validated_data):

        password = validated_data.pop("password")

        # Get Free Plan
        free_plan = Plan.objects.get(name="Free")

        # Create User
        user = User(
            current_plan=free_plan,
            **validated_data
        )

        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)