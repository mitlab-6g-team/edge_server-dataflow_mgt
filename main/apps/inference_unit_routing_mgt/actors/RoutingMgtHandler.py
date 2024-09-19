
"""
RoutingMgtHandler
"""
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger, log_writer
from main.apps.inference_unit_routing_mgt.services.kong_control import add_kong_service, add_kong_route, remove_kong_route, remove_kong_service

@require_POST
@log_trigger("INFO")
def add_routing_data(request):
    """
    add_routing_data 
    """
    data = json.loads(request.body.decode('utf-8'))
    route_status_code = 201
    
    try: 
        log_writer('INFO', add_routing_data, (request,), message="add_routing_data")
        
        service_status_code = add_kong_service(
            service_type=data['service_type'], 
            position_uid=data['position_uid'], 
            service_url=data['service_url']
            )
        
        route_status_code = add_kong_route(
            service_type=data['service_type'],
            position_uid=data['position_uid']
            )
    
    except Exception as e:
        print(e)
    
    if(route_status_code==201):
        return JsonResponse({"msg": "success"}, status=201)
    elif(route_status_code==404):
        return JsonResponse({"msg": "The service name isn't existed"}, status=404)
    elif(route_status_code==409):
        return JsonResponse({"msg": "The route name has already been created"}, status=409)
    

@require_POST
@log_trigger("INFO")
def remove_routing_data(request):
    """
    remove_routing_data 
    """
    data = json.loads(request.body.decode('utf-8'))
    service_status_code = 200
    route_status_code = 200
    
    try:
        log_writer('INFO', remove_routing_data, (request,), message="remove_routing_data")
        
        route_status_code = remove_kong_route(
            service_type=data['service_type'],
            position_uid=data['position_uid']
            )
        service_status_code = remove_kong_service(
            service_type=data['service_type'], 
            position_uid=data['position_uid']
            )
    except Exception as e:
        print(e)
        
    if(service_status_code==204):
        return JsonResponse({"msg": "success"}, status=201)
    elif(route_status_code==404):
        return JsonResponse({"msg": "route not found"}, status=404)
    else: 
        JsonResponse({"msg": "unknown error"})
