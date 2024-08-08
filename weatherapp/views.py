from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Hyderabad'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ec5b6c4e5df460c9fdd26883bb7b460a'
    PARAMS = {'units':'metric'}
    API_KEY = 'AIzaSyAcreFstTsWn8-k2C7UInSuYpQ4Gs7lWs4'
    SEARCH_ENGINE_ID = 'f4e3fbbe4ffb14207'
    query = city + "1920x1080"
    page = 1
    start = (page-1)*10+1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items") 
    image_url = search_items[1]['link']

    try:
        data = requests.get(url, PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request,'./index.html',{'description': description,'icon': icon, 'temp': temp, 'city': city, 'day': day, 'exception_occured': False}) 
        # return render(request, 'index.html')
    
    except KeyError:
        exception_occured = True
        messages.error(request, 'entered data not available to API')
        day = datetime.date.today()
        return render(request,'./index.html',{'description': 'clear sky','icon': '01d', 'temp': 28, 'city': 'Indore', 'day': day, 'exception_occured': True}) 