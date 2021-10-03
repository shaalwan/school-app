from .serializers import *
from .models import User
from django.http.response import Http404
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status  # for response status
from rest_framework import viewsets 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class registerStudent(APIView):
  def post(self,requests):
    admin = requests.user
    if(admin.is_staff==True):
      data = requests.data  # getting data from body
      username = data['username']
      password = data['password']
      registeration_id = data['registeration_id']
      user = User.objects.create_user(username=username, password=password,registeration_id=registeration_id)
      user.standard=data['standard']
      user.name=data['name']
      user.father_name=data['father_name']
      user.roll_number=data['roll_number']
      user.save()
      serializer = UserSerializer(user)
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
      return Response({'error':'user not authorised'}, status=status.HTTP_400_BAD_REQUEST)

class registerAdmin(APIView):
  def post(self,requests):
    data = requests.data 
    username = data['username']
    password = data['password']
    registeration_id = data['registeration_id']
    user = User.objects.create_superuser(username=username, password=password,registeration_id=registeration_id)
    user.name=data['name']
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

class login(APIView):
  def post(self, request, format=None):
        data = request.data
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response({"Error": "invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class Userlistview(viewsets.ReadOnlyModelViewSet):
  model = User
  serializer_class = UserSerializer
  filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
  filterset_fields = ['standard', 'username']
  search_fields = ('username','name','roll_number','registeration_id')
  
  def get_queryset(self):
        users = User.objects.all().order_by('roll_number')
        return users

class userview(APIView):
  def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
  
  def get(self, requests, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

  def put(self, requests, pk):
        user = self.get_object(pk)
        serializer = addUserSerializer(user, data=requests.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, requests, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)