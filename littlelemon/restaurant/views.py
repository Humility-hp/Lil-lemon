from django.shortcuts import render
# from django.http import response
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .models import booking, menu
from .serializers import bookingSerializer, menuSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import permission_classes, authentication_classes

# Create your views here

@api_view()
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def secret(request):
  return Response({"message":"Some secret message"})

def home(request):
  return render(request,"index.html")

# different views
@api_view(['GET','POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def bookingView(request):
  items = booking.objects.all()
  serializer = bookingSerializer(items, many=True)
  return Response(serializer.data)

@api_view(['GET','POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def menuView(request):
  items = menu.objects.all()
  serializer = menuSerializer(items, many=True)
  return Response(serializer.data)

# class menuView(APIView):
#  def post(self, request):
#   serializer = menuSerializer(data=request.data)

#   if serializer.is_valid():
#    serializer.save()
#    return Response({"status":"success", "data":serializer.data})
  
