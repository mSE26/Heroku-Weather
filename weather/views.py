from django.shortcuts import render
import requests
from .models import City
from .models import CityFake
from .forms import CityForm

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c2a3f1958ac6d597a4864a0b94b204b1'

    cities = City.objects.all()
    posts = CityFake.objects.all()
	
    if request.method == 'POST': 
        form = CityForm(request.POST) 
        form.save() 
		
    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() 
        
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) 
    context = {'weather_data' : weather_data, 'CityFake' : posts, 'form' : form}
    return render(request, 'weather/index.html', context)