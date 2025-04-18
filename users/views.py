from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SimpleRegisterSerializer

class SimpleRegisterView(APIView):
    def post(self, request):
        serializer = SimpleRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User registered successfully",
                "user_id": user.user_id,
                "username": user.username
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
