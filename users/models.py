from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from yobale import settings
from colorfield.fields import ColorField
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
from location_field.models.plain import PlainLocationField
from django.core.validators import MaxValueValidator, MinValueValidator


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/passagers/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}passagers/'.format(settings.MEDIA_URL),
)

def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/passagers/profile/<filename>
    return u'profiles/{0}'.format(filename)


TRAINER = "Trainer"
MEMBER = "Member"
PASSAGER = "Passager"
CONDUCTEUR = "Conducteur"
####
DEBUTANT    = 'Debutant'
HABITUE     = 'Habitue'
CONFIRME    = 'Confirme'
EXPERT      = 'Expert'
AMBASSADEUR = 'Ambassadeur'
#### CARBURANT
ESSENCE = 'Essence'
GAZOIL = 'Gazoil'
ELECTRIQUE = 'Electrique'
HYBRIDE = 'Hybride'
#### MODES DE PAIEMENT
CHEQUES = 'Par Chèques'
ESPECES = 'Par espèces'
CB = 'Carte Bancaire'
VIREMENT = 'Par Virement'
TRANSFERT = 'Par Transfert'
#### TYPES LOCALITES
REGION = 'Region'
DEPARTEMENT = 'Departement'
COMMUNE = 'Commune'
VILLAGE = 'Village'
#### STATUES TRAJET
COMPLET = 'Complet'
TERMINE = 'Termine'
ANNULE = 'Annule'
OUVERT = 'Ouvert'
STATUE_TRAJET = [
    (COMPLET, "Complet"),
    (TERMINE, "Termine"),
    (ANNULE, "Annule"),
    (OUVERT, "Ouvert"),
]
TYPE_LOCALITE = [
    (REGION, "Region"),
    (DEPARTEMENT, "Departement"),
    (COMMUNE, "Commune"),
    (VILLAGE, "Village"),
]
# EXPERIENCES
EXPERIENCES =  [
    ( DEBUTANT, 'Debutant'),
    ( HABITUE, 'Habitué'),
    ( CONFIRME, 'Confirmé'),
    ( EXPERT , 'Expert'),
    ( AMBASSADEUR, 'Ambassadeur'),
]
# MODE_PAIEMENT
MODE_PAIEMENT = [
    (CHEQUES, "Paiement par Chèques"),
    (ESPECES, "Paiement par Espèces"),
    (CB, "Paiement par Carte Bancaire"),
    (VIREMENT, "Conducteur"),
    (TRANSFERT, "Conducteur"),
]

DISCUSSION = ((True, 'J\'aime discuter parfois'), (False, 'Je n\'aime pas discuter quand je conduis' ))
FUMEUR = ((True, 'J\'accepte la fumée'), (False, 'Je n\'aime pas la fumée dans la voiture' ))
ANIMAUX = ((True, 'J\'accepte les animaux de compagnie'), (False, 'Je n\'aime pas les animaux de compagnie dans la voiture' ))
MUSIQUE =  ((True, 'J\'aime bien écouter de la musique'), (False, 'Je n\'aime pas écouter de la musique en conduisant' ))

CARBURANT = [
    ( ESSENCE, "Essence"),
    ( GAZOIL, "Gazoil"),
    ( ELECTRIQUE, "Electrique"),
    ( HYBRIDE, "Hybride"),
]

class Role(models.Model):
    role= models.CharField(max_length=30, null=False,blank=False, verbose_name='Role du membre', unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='', verbose_name='Description du role')
    
    class Meta:
        verbose_name = "Role"
        
    def __str__(self):
        return self.role

class StatutTrajet(models.Model):
    status= models.CharField(max_length=30, null=False,blank=False, verbose_name='Statue du trajet', unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Statut Trajet"
        
    def __str__(self):
        return self.status

class Carburant(models.Model):
    carburant_type= models.CharField(max_length=30, null=False,blank=False, verbose_name='CARBURANT', unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Carburant"
        
    def __str__(self):
        return self.carburant_type


class ModePaiement(models.Model):
    mode= models.CharField(max_length=30, null=False,blank=False, verbose_name='Mode de paiement', unique=True)
    created_on = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Mode de Paiement"
        
    def __str__(self):
        return self.mode

# Creation d'un User
class CustomUserManager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, email, password, **extra_fields)

    def create_superuser(
        self, username=None, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, email, password, **extra_fields)

# Extension de l'utilisation Django
class UserAccount(AbstractUser):
    #role = models.CharField(max_length=15, choices=ROLES, default="Passager")
    role = models.ManyToManyField(Role, related_name='roles')
    location = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=10, null=True,blank=True)
    image = models.ImageField(upload_to="user_pics", null=True, blank=True)
    email_verifie = models.BooleanField(default=False)
    experience = models.CharField(max_length=15, choices=EXPERIENCES, default="Debutant")
    discussion = models.BooleanField(choices=DISCUSSION, default=True)
    fumeur = models.BooleanField(choices=FUMEUR, default=False)
    musique = models.BooleanField(choices=MUSIQUE, default=True)
    profile_actif = models.BooleanField(default=False, verbose_name='Profile actif')



    objects = CustomUserManager()
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone_number",
        "discussion",
        "fumeur",
        "musique"
    ]
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.get_full_name()



class Membership(models.Model):
    personne = models.OneToOneField(UserAccount,related_name='members_profiles', limit_choices_to={"role": "Passager"}, on_delete=models.CASCADE)
    date_joined = models.DateField()
    
    class Meta:
        verbose_name = "Membership"
        
    def __str__(self):
        return self.personne

#     user = models.OneToOneField(UserAccount,related_name='trainer_profiles', limit_choices_to={"role": "Trainer"}, on_delete=models.CASCADE)
#     is_disabled = models.BooleanField(default=False, verbose_name='Profile actif')

################# Modeles ORM YOBALE #################

# As model field:
class Voiture(models.Model):
    marque = models.CharField(max_length=200, default='')
    modele = models.CharField(max_length=200, default='')
    couleur = ColorField(default='#FF0000')
    carburant = models.CharField(max_length=15, choices=CARBURANT)
    matricule =  models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    proprietaire = CurrentUserField()
    created_date = models.DateTimeField(default=timezone.now)
    valide = models.BooleanField(default=False)



class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

# Album
class Region(models.Model):
    nom = models.CharField(max_length=70, blank=False, default='', unique=True)
    location = PlainLocationField(based_fields=['nom'], zoom=7, default='', blank=False)
    description = models.CharField(max_length=200,blank=False, default='')

    def __str__(self):
        return f"{self.nom}"

# Track
class Departement(models.Model):

    class Meta:
        verbose_name = "Departement"
        unique_together = ("nom", "region",)
    
    nom = models.CharField(max_length=70, blank=False, default='')
    region = models.ForeignKey(Region, related_name='departements', on_delete=models.CASCADE)
    location = PlainLocationField(based_fields=['nom'], zoom=7, default='', blank=False)
    description = models.CharField(max_length=200,blank=False, default='')


    def __str__(self):
        return f"{self.nom}"

# Etapes de trajet
class Localite(models.Model):
    
    class Meta:
        verbose_name = "Localite"

    type_locatite = models.CharField(max_length=15, choices=TYPE_LOCALITE, default=COMMUNE, verbose_name= 'Type de la localité')
    nom = models.CharField(max_length=70, blank=False, default='', verbose_name= 'Nom de la localité')
    departement = models.ForeignKey(Departement, related_name='localites', on_delete=models.CASCADE)
    description = models.CharField(max_length=200,blank=False, default='')
    
    
    def __str__(self):
        return f"{self.type_locatite} de {self.nom} [ {self.departement} ]"
    
# Trajet
class Trajet(models.Model):
    
    class Meta:
        verbose_name = "Trajet"
        ordering = ['maj', 'date_depart']

    depart = models.ForeignKey(Localite, related_name='depart', on_delete=models.CASCADE)
    destination = models.ForeignKey(Localite, related_name='destination', on_delete=models.CASCADE)
    prix_ht   = models.PositiveIntegerField(verbose_name="Prix unitaire HT")
    prix_ttc   = models.PositiveIntegerField(verbose_name="Prix unitaire HT")
    nb_places = models.PositiveIntegerField(verbose_name="Places disponibles", default=4)
    etapes  = models.ManyToManyField("Localite", related_name="etapes")
    date_depart = models.DateField(verbose_name='Date de départ', default=timezone.now)
    heure_depart = models.TimeField(verbose_name='Heure de départ', blank=True, null=True)
    date_arrivee = models.DateField(verbose_name='Date d\'arrivée', default=timezone.now)
    heure_arrivee  = models.TimeField(verbose_name='Heure d\'arrivée', blank=True, null=True)
    conducteur = CurrentUserField(verbose_name='Conducteur')
    maj = models.DateTimeField(auto_now=True)
    #passagers = models.ManyToManyField('UserAccount', limit_choices_to={"role": "Passager"})
    
    #members = models.ManyToManyField(Membership, limit_choices_to={"profile_actif": True})
    members  = models.ManyToManyField("UserAccount", related_name="members", limit_choices_to={"profile_actif": True})
    statue = models.ForeignKey(StatutTrajet, related_name='statue', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.depart} => {self.destination} Départ le {self.date_depart} à {self.heure_depart} Arrivée le {self.date_arrivee} à {self.heure_arrivee}"


# Avis
class Avis(models.Model):
    contenu = models.TextField(verbose_name='Avis')
    fait_le = models.DateTimeField(auto_now=True)
    trajet = models.ForeignKey(Trajet, related_name='avis', on_delete=models.CASCADE, null=True, blank=True)
    avis_sur = models.CharField(max_length=70, blank=False, default='', verbose_name= 'Avis donné sur')
    auteur = CurrentUserField(verbose_name='Avis fait par')

    class Meta:
        verbose_name = "Avis"

    def __str__(self):
        return f"{self.contenu}"