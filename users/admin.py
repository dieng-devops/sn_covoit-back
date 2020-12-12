from django.contrib import admin

# Register your models here.

from .models import (MemberProfile, NextOfKin, TrainerProfile,
                     TrainerSpeciality, UserAccount)

admin.site.register(UserAccount)
admin.site.register(MemberProfile)
admin.site.register(TrainerProfile)
admin.site.register(TrainerSpeciality)
admin.site.register(NextOfKin)

admin.site.site_header = "gymie admin"
admin.site.site_title = "gymie"
