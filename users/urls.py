from django.urls import path, include,  re_path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter
from .views import *
# End for Members
app_name = 'users'
urlpatterns = [
    # Vehicule
    path('', welcome),    
    path('tutorials', tutorial_list),
    #path('tutorials/(?P<pk>[0-9]+)', tutorial_detail),
    path('tutorials/<int:pk>/', tutorial_detail, name='tutorial_detail'),
    path('tutorials/published', tutorial_list_published),
    # REGIONS
    path('regions', liste_regions),
    path('region/<int:pk>/', get_region_byId, name='region_details'),
    #path('departements/<int:pk>/', get_Departements, name='departements_details'),
    # DEPARTEMENTS
    path('departements', liste_regions),
    path('departement/<int:pk>/', get_region_byId, name='region_details'),
    # AVIS
    path('avis', liste_avis),
    path('avis/<int:pk>/', get_avis_byId, name='avis_details'),
    # TRAJETS
    path('trajets', liste_trajets),
    path('trajet/<int:pk>/', get_trajet_byId, name='trajet_details'),
    # LOCALITES
    path('localites', liste_localites),
    path('localite/<int:pk>/', get_localite_byId, name='localite_details'),
    # 
]