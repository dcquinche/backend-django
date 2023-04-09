from rest_framework import viewsets
from . import models
from . import serializers

class LibreriaViewset(viewsets.ModelViewSet):
    queryset = models.Libreria.objects.all()
    serializer_class = serializers.LibreriaSerializers
