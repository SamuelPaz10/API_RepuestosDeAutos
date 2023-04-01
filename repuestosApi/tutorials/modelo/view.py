from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from tutorials.models import Modelo
from tutorials.serializers import ModeloSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def modelo_list(request):
    if request.method == 'GET':
        modelo = Modelo.objects.all()
        modelo_serializer = ModeloSerializer(modelo, many=True)
        return JsonResponse(modelo_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        modelo_data = JSONParser().parse(request)
        modelo_serializer = ModeloSerializer(data=modelo_data)
        if modelo_serializer.is_valid():
            modelo_serializer.save()
            return JsonResponse(modelo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(modelo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)