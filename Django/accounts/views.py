from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomDetailSerializer

@api_view(['GET','PUT','DELETE'])
def profile(request):
   user = request.user
   if request.method == 'GET':
      serializer = CustomDetailSerializer(instance=user)
      return Response(serializer.data)
   
   if request.method == 'PUT':
      # print(request.data)
      serializer = CustomDetailSerializer(user, data=request.data, partial=True)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      
   if request.method == 'DELETE':
      user = request.user
      user.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)