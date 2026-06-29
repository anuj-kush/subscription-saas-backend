from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Plan
from .serializers import PlanSerializer


class PlanListView(APIView):

    def get(self, request):

        plans = Plan.objects.all()

        serializer = PlanSerializer(plans, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
