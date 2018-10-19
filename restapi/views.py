from django.http import JsonResponse
from django.db.models import Avg, Max, Min
from rest_framework.decorators import api_view
from restapi.models import Clients

MAX_DATE = Clients.objects.aggregate(Max('date'))['date__max']

MIN_DATE = Clients.objects.aggregate(Min('date'))['date__min']

@api_view(['GET'])
def snippet_list(request):
  if request.query_params.get('date', None) is None:
        compvalue = Clients.objects.filter(device='Computers').values('conversion_value').aggregate(Avg('conversion_value'))

        tabvalue = Clients.objects.filter(device='Tablets with full browsers').aggregate(Avg('conversion_value'))

        mobilevalue = Clients.objects.filter(device='Mobile devices with full browsers').aggregate(Avg('conversion_value'))
        
        response = {
            "date": "all",
            "computers": compvalue,
            "tablets": tabvalue,
            "mobile": mobilevalue
        }

  if request.query_params.get('date', None) is not None:
    
        compvalue = Clients.objects.filter(device='Computers', date=request.query_params.get('date', None)).aggregate(Avg('conversion_value'))

        tabvalue = Clients.objects.filter(device='Tablets with full browsers', date=request.query_params.get('date', None)).aggregate(Avg('conversion_value'))

        mobilevalue = Clients.objects.filter(device='Mobile devices with full browsers', date=request.query_params.get('date', None)).aggregate(Avg('conversion_value'))

        response = {
            "date": request.query_params.get('date', None),
            "computers": compvalue,
            "tablets": tabvalue,
            "mobile": mobilevalue
        }

  return JsonResponse({
      "data": response,
      "mindate": MAX_DATE,
      "maxdate": MIN_DATE
  })
