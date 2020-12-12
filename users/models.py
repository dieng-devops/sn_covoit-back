from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

TRAINER = "Trainer"
MEMBER = "Member"
PASSAGER = "Passager"
CONDUCTEUR = "Conducteur"

ROLES = [
    (TRAINER, "Trainer"),
    (MEMBER, "Member"),
    (PASSAGER, "Passager"),
    (CONDUCTEUR, "Conducteur"),
]

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

    objects = CustomUserManager()
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone_number",
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

