from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


from . import serializers, models, permissions


# Create your views here.

class HelloAPIView(APIView):
    """test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional django view',
            'Gives you the most control over your logic',
            'It is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handles updating an object."""
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """deletes an object."""
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'provides more functionality with less code'
        ]

        return Response({'message': 'hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """create a new hello message"""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """handles getting an object by its ID"""
        return Response({'http_method':'GET'})


    def update(self, request, pk=None):
        """handles updating an object"""
        return Response({'http_method':'PUT'})


    def partial_update(self, request, pk=None):
        """handles updating part of an object"""
        return Response({'http_method':'PATCH'})


    def destroy(self, request, pk=None):
        """handles removing of an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    


