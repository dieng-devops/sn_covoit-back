from django.core.exceptions import ObjectDoesNotExist
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import SerializerMethodField
from rest_framework.serializers import CurrentUserDefault, HiddenField, ModelSerializer, StringRelatedField
from .models import TrainerProfile, TrainerSpeciality,  MemberProfile, NextOfKin
from rest_framework.serializers import CurrentUserDefault, HiddenField,  ModelSerializer,  PrimaryKeyRelatedField, StringRelatedField

# Serialiser un User Cutomise
class CustomUserSerializer(UserSerializer):
    """
    Override djoser current user serializer to return abstact user fields
    """
    has_profile = SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = (
            "id",
            'first_name',
            'last_name',
            "role",
            "email",
            "phone_number",
            "location",
            'image',
            "is_superuser",
            "has_profile",
        )

    def get_has_profile(self, obj):
        if obj.role == 'Member':
            # check if the users have profiles associated with them
            try:
                return bool(obj.member_profiles)
            except ObjectDoesNotExist:
                return False

        elif obj.role == 'Trainer':
            try:
                return bool(obj.trainer_profiles)
            except ObjectDoesNotExist:
                return False
        else:
            return None

# serialize member profile for creation
class MemberProfileCreateSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = MemberProfile
        fields = "__all__"


# serialize member's profile
class MemberDetailSerializer(ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = MemberProfile
        fields = "__all__"


# serialize next of kin
class NextOfKinSerializer(ModelSerializer):
    member = StringRelatedField(read_only=True)
    class Meta:
        model = NextOfKin
        fields = "__all__"



# highlights the specialties of a trainer
class TrainerSpecialtySerializer(ModelSerializer):
    class Meta:
        model = TrainerSpeciality
        fields = '__all__'


# allows creation of the trainer profile
class TrainerCreateSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault()) #review later
    class Meta:
        model = TrainerProfile
        fields = '__all__'


# returns an object of trainer profile with user details
class TrainerDetailSerializer(ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    specialities = TrainerSpecialtySerializer(many=True,read_only=True)
    class Meta:
        model = TrainerProfile
        fields = '__all__'

# # highlights the specialties of a trainer
# class TrainerSpecialtySerializer(ModelSerializer):
#     class Meta:
#         model = TrainerSpeciality
#         fields = '__all__'

class UserRegistrationSerializer(UserCreateSerializer):
    """
    Override djoser's usercreation class to accomodate abstract user fields
    """

    class Meta(UserCreateSerializer.Meta):
        fields = (
            "first_name",
            "last_name",
            "role",
            "email",
            "phone_number",
            "location",
            'image',
            'password',
        )

