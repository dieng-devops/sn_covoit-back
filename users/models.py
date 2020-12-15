from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from yobale import settings

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
####
ROLES = [
    (TRAINER, "Trainer"),
    (MEMBER, "Member"),
    (PASSAGER, "Passager"),
    (CONDUCTEUR, "Conducteur"),
]

EXPERIENCES =  [
    ( DEBUTANT, 'Debutant'),
    ( HABITUE, 'Habitué'),
    ( CONFIRME, 'Confirmé'),
    ( EXPERT , 'Expert'),
    ( AMBASSADEUR, 'Ambassadeur'),
]

DISCUSSION = ((True, 'J\'aime discuter parfois'), (False, 'Je n\'aime pas discuter quand je conduis' ))
FUMEUR = ((True, 'J\'accepte la fumée'), (False, 'Je n\'aime pas la fumée dans la voiture' ))
ANIMAUX = ((True, 'J\'accepte les animaux de compagnie'), (False, 'Je n\'aime pas les animaux de compagnie dans la voiture' ))
MUSIQUE =  ((True, 'J\'aime bien écouter de la musique'), (False, 'Je n\'aime pas écouter de la musique en conduisant' ))

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
    role = models.CharField(max_length=15, choices=ROLES, default="Member")
    location = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=10, null=True,blank=True)
    image = models.ImageField(upload_to="user_pics", null=True, blank=True)
    email_verifie = models.BooleanField(default=False)
    experience = models.CharField(max_length=15, choices=EXPERIENCES, default="Debutant")
    discussion = models.BooleanField(choices=DISCUSSION, default=True)
    fumeur = models.BooleanField(choices=FUMEUR, default=False)
    musique = models.BooleanField(choices=MUSIQUE, default=True)

    objects = CustomUserManager()
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone_number",
        "email_verifie",
        "experience",
        "discussion",
        "fumeur",
        "musique"
    ]
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.get_full_name()

# Profile d'un membre simple
class MemberProfile(models.Model):
    user = models.OneToOneField(
        UserAccount, related_name='member_profiles',limit_choices_to={"role": "Member"}, on_delete=models.CASCADE
    )
    is_disabled = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.user}"

# Profile d'un coach
class TrainerProfile(models.Model):
    user = models.OneToOneField(
        UserAccount,related_name='trainer_profiles', limit_choices_to={"role": "Trainer"}, on_delete=models.CASCADE
    )
    description = models.TextField()
    specialities = models.ManyToManyField('TrainerSpeciality')

    def __str__(self):
        return f"{self.user}"

# Specialites d'un Coach
class TrainerSpeciality(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

# Membre le plus proche a aviser
class NextOfKin(models.Model):
    member = models.ForeignKey(
        UserAccount,
        related_name="next_of_kins",
        limit_choices_to={"role": "Member"},
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Creation d'un profile de Passager
class PassagerProfile(models.Model):
    user = models.OneToOneField(
        UserAccount,related_name='passager_profiles', limit_choices_to={"role": "Passager"}, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user}"
