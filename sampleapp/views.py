from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Araba
from .serializers import ArabaSerializer


class ArabaView(APIView):
    def get(self,request):
        if request.GET.get('menzil'):
            arabalar = Araba.objects.all()
            menzil_data=[{"Marka":araba.marka, "Menzil":araba.marka()}for araba in arabalar]
            return Response(menzil_data)

        arabalar = Araba.objects.all()
        serializer=ArabaSerializer(arabalar,many=True)
        return Response(serializer.data)
