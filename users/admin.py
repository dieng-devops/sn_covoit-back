from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(UserAccount)
admin.site.register(MemberProfile)
admin.site.register(TrainerProfile)
admin.site.register(TrainerSpeciality)
admin.site.register(NextOfKin)
admin.site.register(PassagerProfile)
#admin.site.register(ModelTest)
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)


admin.site.site_header = "gymie admin"
admin.site.site_title = "gymie"
