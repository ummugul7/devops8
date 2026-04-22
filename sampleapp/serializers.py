from rest_framework import serializers
from .models import Araba

class ArabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Araba
        fields = ['id','marka','depo','ortalamaHiz','aldigiYol']