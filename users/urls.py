from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'users'
router = DefaultRouter()
router.register('trainer', TrainerAPIView)
# End for Trainer
# Members
router.register('next-of-kin',NextOfKinAPIView)
# End for Members

urlpatterns = [
    ##### REST
    
    path('api/', include(router.urls)),
    # Merbers
    #path('members/',include(router.urls)),
    path("members/all/", MemberListAPIView.as_view()),
    path('members/create/',MemberProfileCreateAPIView.as_view(),name='create_member_profile'),
    path('members/retrieve/<int:pk>/',MemberProfileReadUpdateAPIView.as_view(),name='member_profile_details'),
    # Trainer
    path("trainers/profiles/", include(router.urls)),
    path("trainers/all/", TrainerListAPIView.as_view()),
    path("trainers/specialties/", TrainerSpecialtyListAPIView.as_view()),

]
