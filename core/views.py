from rest_framework.views import APIView
from django.contrib.auth.models import User

from .serializers import UserSerializer
from rest_framework.response import Response

class UserView(APIView):
    def get(self, request, formal=None): # get all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'ok': True, 'data': serializer.data}, status=200)
    
    def post(self, request, formal=None): # create user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            return Response({'ok': True, 'data': serializer.data})
        return Response({'ok': False, 'error': serializer.errors}, status=400)

    def patch(): # change password , change email
        pass