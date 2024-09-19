import requests
from main.utils.env_loader import default_env


def add_kong_service(service_type, position_uid, service_url):
    
    kong_host_ip = default_env.KONG_HOST_IP
    kong_control_port = default_env.KONG_CONTROL_PORT
    service_name = f"""{service_type}-{position_uid}"""
    
    kong_url = f"""http://{kong_host_ip}:{kong_control_port}/services/""" 
    
    headers = {'Accept': 'application/json'}
    data = {'name': service_name , 'url':service_url}
    
    resp = requests.post(kong_url, headers=headers, data=data)
    print(resp.status_code)
    return resp.status_code
    
   
def add_kong_route(service_type, position_uid):
    
    kong_host_ip = default_env.KONG_HOST_IP
    kong_control_port = default_env.KONG_CONTROL_PORT
    service_name = f"""{service_type}-{position_uid}"""
   
    kong_url = f"""http://{kong_host_ip}:{kong_control_port}/services/{service_name}/routes""" 
    headers = {'Accept': 'application/json'}
    
    data = {
        "name": f'{service_name}-route',
        "paths": [f'/{service_name}']
    }
    
    resp = requests.post(kong_url, headers=headers, data=data)
    print(resp.status_code)
    return resp.status_code
    
    
def remove_kong_service(service_type, position_uid):
    
    kong_host_ip = default_env.KONG_HOST_IP
    kong_control_port = default_env.KONG_CONTROL_PORT
    service_name = f"""{service_type}-{position_uid}"""
    
    kong_url = f"""http://{kong_host_ip}:{kong_control_port}/services/{service_name}""" 
    
    resp = requests.delete(kong_url)
    
    return resp.status_code
    
def remove_kong_route(service_type, position_uid):
    
    kong_host_ip = default_env.KONG_HOST_IP
    kong_control_port = default_env.KONG_CONTROL_PORT
    service_name = f"""{service_type}-{position_uid}"""
    
    kong_url = f"""http://{kong_host_ip}:{kong_control_port}/services/{service_name}/routes/{service_name}-route""" 
    
    resp = requests.delete(kong_url)
    
    return resp.status_code
