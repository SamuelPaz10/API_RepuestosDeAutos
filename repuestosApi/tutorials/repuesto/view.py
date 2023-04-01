from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tutorials.models import Repuesto, RepuestoModelos, Modelo
from tutorials.serializers import RepuestoSerializer, RepuestoModelosSerializer, ModeloSerializer

from rest_framework.decorators import api_view
from django.db.utils import IntegrityError

from django.db.models import Count


from pymongo import MongoClient

from tutorials.dbclasses.cliente import ClienteCollection
from django.db.models import Case, When, Value, IntegerField

import pandas as pd

# Create your views here.
@api_view(['POST'])
def repuesto_list(request):
    if request.method == 'POST':
        repuesto_data = JSONParser().parse(request)
        repuesto_serializer = RepuestoSerializer(data=repuesto_data)
        if repuesto_serializer.is_valid():
            repuesto_serializer.save()
            return JsonResponse(repuesto_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(repuesto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def repuesto_detail(request, id):
    repuesto = get_object_or_404(Repuesto, id=id)
    if request.method == 'GET':
        repuesto_serializer = RepuestoSerializer(repuesto)
        return JsonResponse(repuesto_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'PUT':
        repuesto_data = JSONParser().parse(request)
        repuesto_data["id"] = id
        repuesto_serializer = RepuestoSerializer(repuesto, data=repuesto_data)
        if repuesto_serializer.is_valid():
            repuesto_serializer.save()
            return JsonResponse(repuesto_serializer.data)
        return JsonResponse(repuesto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        repuesto.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def repuesto_modelos(request, id):
    repuesto = get_object_or_404(Repuesto, id=id)
    if request.method == 'GET':
        modelos = RepuestoModelos.objects.filter(id_repuesto=repuesto)
        modelos_serializer = RepuestoModelosSerializer(modelos, many=True)
        return JsonResponse(modelos_serializer.data, safe=False)
    
    elif request.method == 'POST':
        modelos_data = JSONParser().parse(request)
        modelos_data["id_repuesto"] = id
        modelos_serializer = RepuestoModelosSerializer(data=modelos_data)
        if modelos_serializer.is_valid():
            modelos_serializer.save()
            return JsonResponse(modelos_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(modelos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def repuesto_modelos_detail(request, id, id_modelo):
    if request.method == 'DELETE':
        repuesto = get_object_or_404(Repuesto, id=id)
        modelo = get_object_or_404(Modelo, id=id_modelo)
        repuesto_modelo = get_object_or_404(RepuestoModelos, id_modelo=modelo, id_repuesto=repuesto)        
        repuesto_modelo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

