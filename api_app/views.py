from django.shortcuts import render

import requests


# Create your views here.
def index(request):
    query = '1lb brisket and fries'
    
    my_headers={'X-Api-Key': 'v/q8BJaQOy88PdffmedUzw==SSfbsGeRYFTzZY2w'}
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    
    response = requests.get(api_url, headers=my_headers)
    # if response.status_code == requests.codes.ok:
    #     print(response.text)
    return render(request,'index.html',{'response':response})
    # else:
    #     print("Error:", response.status_code, response.text)

    
 