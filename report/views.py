from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import DailyFieldReportsSerializer
from .models import DailyFieldReports
# Create your views here.


def index(req):
    return HttpResponse('helo guys how are you')


##############################DailyFieldReportsAPI###############################################33



class DailyFieldReportsAPI(APIView):


    def get(self,request):
        obj=DailyFieldReports.objects.all()
        serializer=DailyFieldReportsSerializer(obj,many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer =DailyFieldReportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


