from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Lingo
from .serializers import LingoSerializer


class LingoListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all the Lingos
        '''
        lingos = Lingo.objects.all()
        serializer = LingoSerializer(lingos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create a Lingo given lingo data, if the user is authenticated
        '''
        if not request.user.is_authenticated:
            return Response({"error": "You must be authenticated to create an item."}, status=401)

        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'lingo_type': request.data.get('lingo_type') or "none",
        }
        serializer = LingoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
