

from .base_settings import *

#ssm = boto3.client("ssm", region_name='ap-southeast-1')
#SECRET_KEY = ssm.get_parameter(Name="/django-lightsail-key", WithDecryption=True)["Parameter"]["Value"]

DEBUG = False