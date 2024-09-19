from django.urls import path
from main.apps.inference_unit_routing_mgt.actors import RoutingMgtHandler

module_name = 'inference_unit_routing_mgt'

urlpatterns = [
    path(f'{module_name}/RoutingMgtHandler/add_routing_data', RoutingMgtHandler.add_routing_data),
    path(f'{module_name}/RoutingMgtHandler/remove_routing_data', RoutingMgtHandler.remove_routing_data)
]