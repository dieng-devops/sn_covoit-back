from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView,  CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
import datetime
from datetime import date, datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

User = get_user_model()
# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def welcome(request):
  content = { 'message': 'Bienvenue dans l\'API YOBALE' }
  return JsonResponse(content, status=200)

###################  TUTORIALS  ###################

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

###################  END TUTORIALS  ###################
###################  REGION  ###################
@api_view(['GET', 'POST', 'DELETE'])
def liste_regions(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        
        nom = request.query_params.get('nom', None)
        departements = request.query_params.get('departements', None)
        if nom is not None:
            regions = regions.filter(nom__icontains=nom)
        if departements is not None:
            regions = regions.filter(departements__nom__icontains=departements)
            # Author.objects.filter(
            #     Q(articles__category='Tech') &
            #     Q(articles__title__startswith='Django')
            # )
        # if departement is not None:
        #     departement = departement.get('nom')
        #     regions = regions.filter(departement__icontains=departement)
        
        regions_serializer = RegionSerializer(regions, many=True)
        return JsonResponse(regions_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        region_data = JSONParser().parse(request)
        region_serializer = RegionSerializer(data=region_data)
        if region_serializer.is_valid():
            region_serializer.save()
            return JsonResponse(region_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Region.objects.all().delete()
        return JsonResponse({'message': '{} Regions sont supprimées avec succès !'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def get_region_byId(request, pk):
    try:
        region = Region.objects.get(pk=pk) 
    except Region.DoesNotExist: 
        return JsonResponse({'message': 'Une Région portant cet Identifiant n\'existe pas'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        region_serializer = RegionSerializer(region) 
        return JsonResponse(region_serializer.data) 
 
    elif request.method == 'PUT': 
        region_data = JSONParser().parse(request) 
        region_serializer = RegionSerializer(region, data=region_data) 
        if region_serializer.is_valid(): 
            region_serializer.save() 
            return JsonResponse(region_serializer.data) 
        return JsonResponse(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        region.delete() 
        return JsonResponse({'message': 'Les Regions sont supprimées avec succès !'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def get_Departements(request, pk):
#     departements = Region.objects.get(pk=pk).departement_set.all()
        
#     if request.method == 'GET': 
#         departements_serializer = RegionSerializer(departements, many=True)
#         return JsonResponse(departements_serializer.data, safe=False)

###################  DEPARTEMENTS  ###################
@api_view(['GET', 'POST', 'DELETE'])
def liste_departements(request):
    if request.method == 'GET':
        departements = Departement.objects.all()
        
        nom = request.query_params.get('nom', None)
        region = request.query_params.get('region', None)
        if nom is not None:
            departements = departements.filter(nom__icontains=nom)
        if region is not None:
            departements = departements.filter(region__icontains=region)
        
        departements_serializer = DepartementSerializer(departements, many=True)
        return JsonResponse(departements_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        departement_data = JSONParser().parse(request)
        departement_serializer = DepartementSerializer(data=departement_data)
        if departement_serializer.is_valid():
            departement_serializer.save()
            return JsonResponse(departement_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(departement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Departement.objects.all().delete()
        return JsonResponse({'message': '{} Departements sont supprimées avec succès !'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def get_departement_byId(request, pk):
    try:
        departement = Departement.objects.get(pk=pk) 
    except Departement.DoesNotExist: 
        return JsonResponse({'message': 'Un Departement portant cet Identifiant n\'existe pas'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        departement_serializer = DepartementSerializer(departement) 
        return JsonResponse(departement_serializer.data) 
 
    elif request.method == 'PUT': 
        departement_data = JSONParser().parse(request) 
        departement_serializer = DepartementSerializer(departement, data=departement_data) 
        if departement_serializer.is_valid(): 
            departement_serializer.save() 
            return JsonResponse(departement_serializer.data) 
        return JsonResponse(departement_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        departement.delete() 
        return JsonResponse({'message': 'Les Departements sont supprimées avec succès !'}, status=status.HTTP_204_NO_CONTENT)

###################  AVIS  ###################
@api_view(['GET', 'POST', 'DELETE'])
def liste_avis(request):
    if request.method == 'GET':
        avis = Avis.objects.all()
        
        id_avis = request.query_params.get('id', None)
        avis_sur = request.query_params.get('avis_sur', None)
        if id_avis is not None:
            avis = avis.filter(id__icontains=id_avis)
        if avis_sur is not None:
            avis = avis.filter(avis_sur__exact = str(avis_sur))
        
        avis_serializer = AvisSerializer(avis, many=True)
        return JsonResponse(avis_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        avis_data = JSONParser().parse(request)
        avis_serializer = AvisSerializer(data=avis_data)
        if avis_serializer.is_valid():
            avis_serializer.save()
            return JsonResponse(avis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(avis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Avis.objects.all().delete()
        return JsonResponse({'message': '{} Avis sont supprimées avec succès !'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def get_avis_byId(request, pk):
    try:
        avis = Avis.objects.get(pk=pk) 
    except Avis.DoesNotExist: 
        return JsonResponse({'message': 'Un Avis portant cet Identifiant n\'existe pas'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        avis_serializer = AvisSerializer(avis) 
        return JsonResponse(avis_serializer.data) 
 
    elif request.method == 'PUT': 
        avis_data = JSONParser().parse(request) 
        avis_serializer = AvisSerializer(avis, data=avis_data) 
        if avis_serializer.is_valid(): 
            avis_serializer.save() 
            return JsonResponse(avis_serializer.data) 
        return JsonResponse(avis_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        avis.delete() 
        return JsonResponse({'message': 'Les Avis sont supprimées avec succès !'}, status=status.HTTP_204_NO_CONTENT)

###################  TRAJETS  ###################
@api_view(['GET', 'POST', 'DELETE'])
def liste_trajets(request):
    if request.method == 'GET':
        trajets = Trajet.objects.all()
        # Rechercher par ID
        id_trajet = request.query_params.get('id', None)
        # Rechercher par Statue du Trajet
        statue = request.query_params.get('statue', None)
        # Rechercher par Point de départ du Trajet
        depart = request.query_params.get('depart', None)
        # Rechercher par point de destination du Trajet
        destination = request.query_params.get('destination', None)
        # Rechercher par Etape du Trajet
        etapes = request.query_params.get('etapes', None)
        # Rechercher par Departement de Départ du Trajet
        departement = request.query_params.get('departement', None)
        #date_depart = request.query_params.get('date_depart', None)
        # Verifier Si le parametre est defini ou pas
        if id_trajet is not None:
            trajets = trajets.filter(id__icontains=id_trajet)
        if statue is not None:
            trajets = trajets.filter(statue__exact = str(statue))
        if depart is not None:
            trajets = trajets.filter(depart__nom__icontains=depart)
        if destination is not None:
            trajets = trajets.filter(destination__nom__icontains=destination)
        if etapes is not None:
            trajets = trajets.filter(etapes__nom__icontains=etapes)
        if etapes is not None:
            trajets = trajets.filter(etapes__nom__icontains=etapes)
        if departement is not None:
            trajets = trajets.filter(depart__departement__nom__icontains=departement)
            
        trajets_serializer = TrajetSerializer(trajets, many=True)
        return JsonResponse(trajets_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        trajet_data = JSONParser().parse(request)
        trajet_serializer = TrajetSerializer(data=trajet_data)
        if trajet_serializer.is_valid():
            trajet_serializer.save()
            return JsonResponse(trajet_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(trajet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Trajet.objects.all().delete()
        return JsonResponse({'message': '{} Trajets sont supprimées avec succès !'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def get_trajet_byId(request, pk):
    try:
        trajet = Trajet.objects.get(pk=pk) 
    except Trajet.DoesNotExist: 
        return JsonResponse({'message': 'Un Trajet portant cet Identifiant n\'existe pas'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        trajet_serializer = TrajetSerializer(trajet) 
        return JsonResponse(trajet_serializer.data) 
 
    elif request.method == 'PUT': 
        trajet_data = JSONParser().parse(request) 
        trajet_serializer = TrajetSerializer(trajet, data=trajet_data) 
        if trajet_serializer.is_valid(): 
            trajet_serializer.save() 
            return JsonResponse(trajet_serializer.data) 
        return JsonResponse(trajet_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        region.delete() 
        return JsonResponse({'message': 'Les Trajets sont supprimées avec succès !'}, status=status.HTTP_204_NO_CONTENT)

###################  LOCALITES  ###################
@api_view(['GET', 'POST', 'DELETE'])
def liste_localites(request):
    if request.method == 'GET':
        localites = Localite.objects.all()
        
        nom = request.query_params.get('nom', None)
        type_locatite = request.query_params.get('type_locatite', None)
        departement = request.query_params.get('departement', None)
        if nom is not None:
            localites = localites.filter(nom__icontains=nom)
        if type_locatite is not None:
            localites = localites.filter(type_locatite__icontains=type_locatite)
        if departement is not None:
            localites = localites.filter(departement__icontains=departement)
        
        localites_serializer = LocaliteSerializer(localites, many=True)
        return JsonResponse(localites_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        localite_data = JSONParser().parse(request)
        localite_serializer = LocaliteSerializer(data=localite_data)
        if localite_serializer.is_valid():
            localite_serializer.save()
            return JsonResponse(localite_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(localite_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Localite.objects.all().delete()
        return JsonResponse({'message': '{} Localites sont supprimées avec succès !'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def get_localite_byId(request, pk):
    try:
        localite = Localite.objects.get(pk=pk) 
    except Localite.DoesNotExist: 
        return JsonResponse({'message': 'Une Localite portant cet Identifiant n\'existe pas'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        localite_serializer = LocaliteSerializer(localite) 
        return JsonResponse(localite_serializer.data) 
 
    elif request.method == 'PUT': 
        localite_data = JSONParser().parse(request) 
        localite_serializer = LocaliteSerializer(localite, data=localite_data) 
        if localite_serializer.is_valid(): 
            localite_serializer.save() 
            return JsonResponse(localite_serializer.data) 
        return JsonResponse(localite_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        localite.delete() 
        return JsonResponse({'message': 'Les Localites sont supprimées avec succès !'}, status=status.HTTP_204_NO_CONTENT)