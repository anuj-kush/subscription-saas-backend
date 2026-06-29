from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    plan = serializers.StringRelatedField()

    class Meta:
        model = Subscription
        fields = [
            "id",
            "user",
            "plan",
            "start_date",
            "end_date",
            "status",
            "created_at",
        ]


class SubscribeSerializer(serializers.Serializer):

    plan_id = serializers.IntegerField()


class UpgradePlanSerializer(serializers.Serializer):

    plan_id = serializers.IntegerField()