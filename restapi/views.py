from django.http import JsonResponse
from restapi.models import Clients
from rest_framework.decorators import api_view

@api_view(['GET'])
def snippet_list(request):
  if request.method == 'GET' and request.query_params.get('date', None)== None:
    return JsonResponse({"models_to_return": list(Clients.objects.values())})

  if request.method == 'GET' and request.query_params.get('date', None) != None: 	
    return JsonResponse({"data": list(Clients.objects.filter(date=request.query_params.get('date', None)).values())})
