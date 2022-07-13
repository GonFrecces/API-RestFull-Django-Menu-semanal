from urllib import request
from django.shortcuts import render
from ACME_APP.models import *
from rest_framework import viewsets
from .serializers import MenuSerializers, PlatoSerializers,IngredientesSerializers,PlatosSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

def API_VIEW(request):
    return render(request,"Home/index.html")



class MenusViewsets(viewsets.ReadOnlyModelViewSet):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

    @action(detail=False, methods=['get'])
    def Platos(self, request):
        id__plato = request.query_params.get('id')
        print(id__plato)
        plato = Plato.objects.filter(Id_plato=id__plato)
        sr = PlatoSerializers(plato, many=True)
        return Response({'data': sr.data})
    
    @action(detail=False, methods=['get'])
    def Ingredientes(self, request, pk=None):
        id__ingrediente = request.query_params.get('id')
        print(id__ingrediente)
        plato = Ingredientes.objects.filter(Plato=id__ingrediente)
        sr = IngredientesSerializers(plato, many=True)
        return Response({'data': sr.data})

   
    
class PlatoViewsets(viewsets.ReadOnlyModelViewSet):

    queryset = Plato.objects.all()
    serializer_class = PlatosSerializers

    

class IngredientesViewsets(viewsets.ModelViewSet):

    queryset = Ingredientes.objects.all()
    serializer_class = IngredientesSerializers
    
    def destroy(self, request, pk=None):
        """
        Elimina un Ingrediente por id

        Eliminar ingrediente
        """
        ingrediente = self.get_object()
        ingrediente.delete()
        # you custom logic #
        return Response({"Mensaje": "Ingrediente eliminado con exito."})

