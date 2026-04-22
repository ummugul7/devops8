from django.db import models

# Create your models here.

class Araba(models.Model):
    marka=models.CharField(max_length=100)
    depo=models.IntegerField()
    ortalamaHiz=models.IntegerField()
    aldigiYol=models.FloatField()

    def menzil(self):
        return str(int(100 * (self.depo / self.ortalama_yakit()))) + " km"

    def ortalama_yakit(self):
        if self.ortalamaHiz <=100:
            return 7
        elif self.ortalamaHiz <= 130:
            return 8
        elif self.ortalamaHiz <= 150:
            return 9
        elif self.ortalamaHiz <= 180:
            return 10
        elif self.ortalamaHiz <= 200:
            return 12
        else:
            return 15


    def __str__(self):
        return self.marka