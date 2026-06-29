from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Subscription
from .serializers import SubscribeSerializer, UpgradePlanSerializer
from plans.models import Plan


class SubscribeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = SubscribeSerializer(data=request.data)

        if serializer.is_valid():

            plan_id = serializer.validated_data["plan_id"]

            try:
                plan = Plan.objects.get(id=plan_id)
            except Plan.DoesNotExist:
                return Response(
                    {"error": "Plan not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Cancel any existing active subscription
            Subscription.objects.filter(
                user=request.user,
                status="ACTIVE"
            ).update(status="CANCELLED")

            # Create new active subscription
            Subscription.objects.create(
                user=request.user,
                plan=plan,
                status="ACTIVE"
            )

            # Update user's current plan
            request.user.current_plan = plan
            request.user.save()

            return Response(
                {
                    "message": "Subscription Successful",
                    "plan": plan.name
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class UpgradePlanView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):

        serializer = UpgradePlanSerializer(data=request.data)

        if serializer.is_valid():

            plan_id = serializer.validated_data["plan_id"]

            try:
                plan = Plan.objects.get(id=plan_id)
            except Plan.DoesNotExist:
                return Response(
                    {"error": "Plan not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Get latest active subscription
            subscription = Subscription.objects.filter(
                user=request.user,
                status="ACTIVE"
            ).order_by("-start_date").first()

            if not subscription:
                return Response(
                    {"error": "No active subscription found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            subscription.plan = plan
            subscription.save()

            request.user.current_plan = plan
            request.user.save()

            return Response(
                {
                    "message": "Plan upgraded successfully",
                    "new_plan": plan.name
                }
            )

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class CancelSubscriptionView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        subscription = Subscription.objects.filter(
            user=request.user,
            status="ACTIVE"
        ).order_by("-start_date").first()

        if not subscription:
            return Response(
                {"error": "No active subscription found"},
                status=status.HTTP_404_NOT_FOUND
            )

        subscription.status = "CANCELLED"
        subscription.save()

        free_plan = Plan.objects.get(name="Free")
        request.user.current_plan = free_plan
        request.user.save()

        return Response({
            "message": "Subscription Cancelled Successfully"
        })


class CurrentSubscriptionView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        subscription = Subscription.objects.filter(
            user=request.user,
            status="ACTIVE"
        ).order_by("-start_date").first()

        if not subscription:
            return Response(
                {"error": "No active subscription"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response({
            "plan": subscription.plan.name,
            "status": subscription.status,
            "expiry": subscription.end_date
        })