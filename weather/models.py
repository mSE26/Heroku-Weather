from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)
	
    def __str__(self): 
        return self.name

    class Meta: 
        verbose_name_plural = 'cities'

class CityFake(models.Model):
    name = models.CharField(max_length=25)
    temp = models.CharField(max_length=25)
    disc = models.CharField(max_length=25)
    def __str__(self): 
        return self.name

    class Meta: 
        verbose_name_plural = 'citiesFake'
		