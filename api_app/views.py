from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json

def home(request):
    url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2022-06-01&'
       'sortBy=popularity&'
       'apiKey=a6aba2d161234810abdf29e32db175dd')

    response = requests.get(url)
    text = json.dumps(home, sort_keys=True, indent=4)
    print(text)

    print(response.json())


    return render(request, 'api_app/index.html', {
        "author": "Al Root",
        'name': "Barron's",
    })
    
    

    # create a formatted string of the Python JSON object
    
# Create your views here.
