"""
load env
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(".env.common")
load_dotenv()

@dataclass
class Default:
    """
        load default env
    """
    LOGS_FOLDER_PATH:str
    DJANGO_SETTINGS_MODULE:str
    DEBUG:str
    ALLOWED_HOSTS:str
    API_ROOT:str
    API_VERSION:str
    KONG_HOST_IP:str
    KONG_CONTROL_PORT:str

default_env = Default(
    LOGS_FOLDER_PATH=os.environ.get('LOGS_FOLDER_PATH'),
    DJANGO_SETTINGS_MODULE=os.environ.get('DJANGO_SETTINGS_MODULE'),
    DEBUG=os.environ.get('DEBUG'),
    ALLOWED_HOSTS=os.environ.get('ALLOWED_HOSTS'),
    API_ROOT=os.environ.get('API_ROOT'),
    API_VERSION=os.environ.get('API_VERSION'),
    KONG_HOST_IP=os.environ.get('KONG_HOST_IP'),
    KONG_CONTROL_PORT=os.environ.get('KONG_CONTROL_PORT')
)