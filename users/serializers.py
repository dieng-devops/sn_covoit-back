from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import SerializerMethodField, CurrentUserDefault, HiddenField,  ModelSerializer,  PrimaryKeyRelatedField, StringRelatedField
from rest_framework.relations import HyperlinkedIdentityField
from .models import *

# Serializer for Roles
class RoleSerializer(ModelSerializer):
    
    class Meta:
        model = Role
        fields = ['id', 'role', 'created_on', 'description']


# Serialiser un User Cutomise
class CustomUserSerializer(UserSerializer):
    """
    Override djoser current user serializer to return abstact user fields
    """
    has_profile = SerializerMethodField()
    role = RoleSerializer(many=True, read_only=True)

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
            "email_verifie",
            'experience',
            'discussion',
            'fumeur',
            'musique',
            'profile_actif',
        )

    def get_has_profile(self, obj):
        if obj.role == 'Conducteur':
            try:
                #return bool(obj.conducteur_profiles)
                return True
            except ObjectDoesNotExist:
                return False

        elif obj.role == 'Passager':
            try:
                #return bool(obj.passager_profiles)
                return True
            except ObjectDoesNotExist:
                return False
        else:
            return None

# # highlights the specialties of a trainer
# class TrainerSpecialtySerializer(ModelSerializer):
#     class Meta:
#         model = TrainerSpeciality
#         fields = '__all__'

class UserRegistrationSerializer(UserCreateSerializer):
    """
    Override djoser's usercreation class to accomodate abstract user fields
    """

    #role = Roll(many=True, read_only=True)
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
            "email_verifie",
            'experience',
            'discussion',
            'fumeur',
            'musique',
            'profile_actif',
        )


class VoitureSerializer(ModelSerializer):
  class Meta:
    model = Voiture
    fields = ['id','marque', 'modele', 'couleur', 'carburant', 'matricule', 'description', 'proprietaire', 'created_date', 'valide']
 
class TutorialSerializer(ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


class DepartementSerializer(ModelSerializer):

    #localites = LocaliteSerializer(many=True, read_only=True)
    class Meta:
        model = Departement
        fields = ['id', 'nom', 'location', 'description']

# Serializer for Avis
class LocaliteSerializer(ModelSerializer):
    
    departement = DepartementSerializer(read_only=True)
    class Meta:
        model = Localite
        fields = ['id', 'type_locatite', 'nom', 'departement', 'description']

# Serializer for Region
class RegionSerializer(ModelSerializer):
    # departements = StringRelatedField(many=True)
    departements = DepartementSerializer(many=True, read_only=True)
    #id  = HyperlinkedIdentityField(view_name='get_region_byId', read_only=True,lookup_field='id',)
    
    class Meta:
        model = Region
        fields = ['id', 'nom', 'location', 'description', 'departements']

# Serializer for Avis
class AvisSerializer(ModelSerializer):
    auteur = UserSerializer()
    class Meta:
        model = Avis
        fields = ['id', 'contenu', 'fait_le', 'avis_sur', 'auteur']

# Serializer for Statut Trajet
class StatutSerializer(ModelSerializer):
    class Meta:
        model = StatutTrajet
        fields = ['id', 'status', 'created_on']

class TrajetSerializer(ModelSerializer):
    etapes = StringRelatedField(many=True)
    #etapes = LocaliteSerializer(read_only=True)
    avis = AvisSerializer(many=True, read_only=True)
    depart = LocaliteSerializer()
    destination = LocaliteSerializer()
    conducteur = UserSerializer() 
    #passagers = UserSerializer()    
    statue = StatutSerializer(read_only=True)

    class Meta:
        model = Trajet
        fields = ['id', 'depart', 'destination', 'prix_ht', 'prix_ttc', 
                'nb_places', 'etapes', 'date_depart', 'heure_depart', 
                'date_arrivee', 'heure_arrivee', 'conducteur', 'maj', 'avis', 'statue']


