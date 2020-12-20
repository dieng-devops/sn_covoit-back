from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(UserAccount)
admin.site.register(Voiture)
admin.site.register(Tutorial)
admin.site.register(Region)
admin.site.register(Departement)
admin.site.register(Localite)
admin.site.register(Avis)
admin.site.register(Membership)
admin.site.register(Role)
admin.site.register(StatutTrajet)
admin.site.register(Trajet)

####


admin.site.site_header = "Yobale admin"
admin.site.site_title = "Yobale"

