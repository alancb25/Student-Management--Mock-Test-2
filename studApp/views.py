from django.shortcuts import render
from studApp.models import StdModel,User
from studApp.serializers import StudentSerializer, UserSerializer,UserListSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import authentication, permissions
from rest_framework import permissions,authentication

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


# Create your views here.

# create student
class UserCreateView(ListCreateAPIView):
    serializer_class=UserSerializer

# profile create
class ProfileCreateView(ListCreateAPIView):
    serializer_class=StudentSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)

        filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
        filterset_fields = ['fee']
        search_fields = ['name','course','joining_date']
        ordering_fields = ['joining_date','fee']

    def get_queryset(self):
        return StdModel.objects.filter(name=self.request.user)

class AllStudentListView(ListAPIView):
    serializer_class=StudentSerializer
    authentication_classes=[authentication.TokenAuthentication] 
    permission_classes=[permissions.IsAuthenticated]
    queryset=StdModel.objects.all()


class ProfileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    queryset=StdModel.objects.all()
    lookup_url_kwarg="pk"

class DeleteStudentView(RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    queryset=StdModel.objects.all()
    lookup_url_kwarg="pk"

class UserListView(ListAPIView):
    serializer_class=UserListSerializer 
    queryset=User.objects.all()