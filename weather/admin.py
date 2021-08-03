from django.contrib import admin
from .models import City
from .models import CityFake

admin.site.register(City)
admin.site.register(CityFake)