from rest_framework import routers
from ACME_APP.views import *
from django.urls import path, include




router = routers.DefaultRouter()
router.register(r'menu', MenusViewsets, basename= 'menu')
router.register(r'plato', PlatoViewsets, basename= 'plato')
router.register(r'Ingredientes', IngredientesViewsets, basename= 'ingredientes')



urlpatterns = [
   path('', include(router.urls)),
]