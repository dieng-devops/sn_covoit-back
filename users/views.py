from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView,  CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

User = get_user_model()
# Create your views here.

# creation of a member profile's
class MemberProfileCreateAPIView(CreateAPIView):
    serializer_class = MemberProfileCreateSerializer
    queryset = MemberProfile.objects.all()


# update/read member's profile
class MemberProfileReadUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MemberDetailSerializer
    queryset = MemberProfile.objects.all()

    # get a member's profile from the api
    def get_object(self):
        user_id = self.kwargs["pk"]
        profile = MemberProfile.objects.get(user__id=user_id)
        return profile

# returns a list of all Members
class MemberListAPIView(ListAPIView):
    queryset = User.objects.filter(role='Member')
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny,]

# create member's next of kin
class NextOfKinAPIView(ModelViewSet):
    serializer_class = NextOfKinSerializer
    queryset = NextOfKin.objects.all()
    # http_method_names =['post','put','delete','options']

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(member=user)
        return serializer.save(member=user)

# returns a list of all Trainers
class TrainerListAPIView(ListAPIView):
    queryset = User.objects.filter(role='Trainer')
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny,]


# creation and update of a trainer's profile
class TrainerAPIView(ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = TrainerProfile.objects.all()
    lookup_field = 'user__id'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TrainerCreateSerializer
        return TrainerDetailSerializer

# retrieves a list of all the trainer's specialties
class TrainerSpecialtyListAPIView(ListAPIView):
    serializer_class = TrainerSpecialtySerializer
    queryset = TrainerSpeciality.objects.all()

############# REST
