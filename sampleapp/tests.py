from http.client import responses

from django.test import TestCase
import unittest
from sampleapp.models import Araba
from unittest.mock import patch
from parameterized import parameterized
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from sampleapp.serializers import ArabaSerializer


class ArabaViewTest(unittest.TestCase):
    def setUp(self):
        self.client = APIClient() #REST API'yi test için simüle eder

    def test_get_all_arabalar(self):
        response = self.client.get(reverse('araba-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        arabalar = Araba.objects.all()
        serializer = ArabaSerializer(arabalar,many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(2, len(serializer.data))

class ArabaTest(unittest.TestCase):
    def setUp(self): # her bir birim testinden önce çağrılacak
        self.araba = Araba(
            marka="Fiat",
            depo =40,
            ortalamaHiz=98,
            aldigiYol=1250

        )
    @patch.object(Araba,'ortalama_yakit',return_value=7) # taklit nesnesi yerleştirdik
    def test_menzil(self,mock_ortalama_yakit): #enjekte ettiğimiz mockun adı
        self.assertEqual(self.araba.menzil(),  "571 km")  # kendi oluşturugun veriyi test ediyor

    @parameterized.expand([
        (50, 7),
        (110, 8),
        (140, 9),
        (160, 10),
        (195, 12),
        (220, 15),
    ])
    def test_ortalama_yakit1(self,ortalama_hiz,beklenenYakit):
        araba = Araba(
            marka="Toyota",
            depo=50,
            ortalamaHiz=ortalama_hiz,
            aldigiYol=1000

        )
        self.assertEqual(araba.ortalama_yakit(), beklenenYakit)



