from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Lingo, LingoType
from .serializers import LingoSerializer, LingoTypeSerializer


class LingoApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all the Lingos
        '''
        lingos = Lingo.objects.all()
        serializer = LingoSerializer(
            lingos, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LingoRandomApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        Get a random Lingo
        '''
        lingo = Lingo.objects.order_by('?').first()
        serializer = LingoSerializer(
            lingo, context={'request': request}, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LingoTypeApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all the LingoTypes
        '''
        lingo_types = LingoType.objects.all()
        serializer = LingoTypeSerializer(
            lingo_types, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
