from rest_framework import serializers 
from tutorials.models import Tutorial,Cliente, Genero, Cliente, Modelo,Repuesto, RepuestoModelos


#class TutorialSerializer(serializers.ModelSerializer):

#   class Meta:
#        model = Tutorial
#        fields = ('id',
#                  'title',
#                  'description',
#                  'published')

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('id', 'nombre', 'descripcion')

class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        fields = ('id', 'descripcion')

class ClienteSerializer(serializers.ModelSerializer):
    def validate_id(self, value):
        # Verifica si ya existe un registro con este id en la base de datos
        if Cliente.objects.filter(id=value).exists():
            raise serializers.ValidationError('Ya existe un owner con este id')
        return value
    
    class Meta:
        model = Cliente
        fields = ('id', 'id_nacional','nombre', 'apellido', 'direccion', 'telefono', 'fecha_nacimiento', 'email', 'id_genero')

class RepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = ('id', 'id_modelo','id_anio' 'nombre', 'descripcion', 'precio')

class RepuestoModelosSerializer(serializers.ModelSerializer):
    modelo = serializers.CharField(source='id_modelo.descripcion', read_only=True)
    class Meta:
        model = RepuestoModelos
        fields = ('id', 'id_repuesto', 'id_modelo', 'modelo')