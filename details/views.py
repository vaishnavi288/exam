
from django.shortcuts import render,get_object_or_404
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from details.models import student
from details.serializers import studentserializer
from details.permissions import AuthenticatedORIS_Superuser
# Create your views hereu.
class Lc(APIView):
    permission_classes=[AuthenticatedORIS_Superuser]
    authentication_classes=[TokenAuthentication]
    def get(self,request):
        a=student.objects.all()
        serializer_instance=studentserializer(a,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer_instance=studentserializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class RUD(APIView):
    permission_classes=[AuthenticatedORIS_Superuser]
    authentication_classes=[TokenAuthentication]
    def get(self,request,i):
        a=get_object_or_404(student,id=i)
        self.check_object_permissions(request,a)
        serializer_instance=studentserializer(a)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


    def put(self,request,i):
        a=get_object_or_404(student,id=i)
        self.check_object_permissions(request,a)
        serializer_instance=studentserializer(a,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)    
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

 
    def patch(self,request,i):
        a=get_object_or_404(student,id=i)
        self.check_object_permissions(request,a)
        serializer_instance=studentserializer(a,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)    
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request,i):
        a=get_object_or_404(student,id=i)
        self.check_object_permissions(request,a) 
        a.delete()
        return Response('deleted')
