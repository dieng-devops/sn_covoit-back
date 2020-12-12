from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'users'
# Trainer
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MemberListAPIView, TrainerAPIView, TrainerListAPIView, TrainerSpecialtyListAPIView, MemberProfileCreateAPIView, MemberProfileReadUpdateAPIView, NextOfKinAPIView
router = DefaultRouter()
router_member = DefaultRouter()
router.register("", TrainerAPIView)
# End for Trainer
# Members
router_member.register('next-of-kin',NextOfKinAPIView)
# End for Members
urlpatterns = [
    # Merbers
    path('members/',include(router_member.urls)),
    path("members/all/", MemberListAPIView.as_view()),
    path('members/create/',MemberProfileCreateAPIView.as_view(),name='create_member_profile'),
    path('members/retrieve/<int:pk>/',MemberProfileReadUpdateAPIView.as_view(),name='member_profile_details'),
    # Trainer
    path("trainers/profiles/", include(router.urls)),
    path("trainers/all/", TrainerListAPIView.as_view()),
    path("trainers/specialties/", TrainerSpecialtyListAPIView.as_view()),
]