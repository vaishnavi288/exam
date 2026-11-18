from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import userserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class registration(APIView):
    def post(self,request):
        serializer_instance=userserializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class logout(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request):
        request.user.auth_token.delete()
        return Response("logout successfuly")