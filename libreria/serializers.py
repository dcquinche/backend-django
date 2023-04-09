from rest_framework import serializers
from .models import Libreria

class LibreriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libreria
        fields = '__all__'
