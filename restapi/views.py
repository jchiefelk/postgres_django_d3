from django.http import JsonResponse
from restapi.models import Clients
from rest_framework.decorators import api_view
from django.db.models import Avg

@api_view(['GET'])
def snippet_list(request):
  if request.method == 'GET' and request.query_params.get('date', None) == None:

    compvalue = Clients.objects.filter(device='Computers').values('conversion_value').aggregate(Avg('conversion_value'))

    tabvalue = Clients.objects.filter(device='Tablets with full browsers').aggregate(Avg('conversion_value'))

    mobilevalue = Clients.objects.filter(device='Mobile devices with full browsers').aggregate(Avg('conversion_value'))

    response = {
      "date": "all",
      "computers": compvalue,
      "tablets": tabvalue,
      "mobile": mobilevalue
    }

  if request.method == 'GET' and request.query_params.get('date', None) != None:
    
    compvalue = Clients.objects.filter(device='Computers',date=request.query_params.get('date', None)).aggregate(Avg('conversion_value'))

    tabvalue = Clients.objects.filter(device='Tablets with full browsers',date=request.query_params.get('date', None)).aggregate(Avg('conversion_value'))

    mobilevalue = Clients.objects.filter(device='Mobile devices with full browsers',date=request.query_params.get('date', None)).aggregate(Avg('conversion_value'))

    response = {
      "date": request.query_params.get('date', None),
      "computers": compvalue,
      "tablets": tabvalue,
      "mobile": mobilevalue
    }

  return JsonResponse({
    "data": response 
  })
