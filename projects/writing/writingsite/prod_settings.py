

from .base_settings import *
import boto3

#ssm = boto3.client("ssm", region_name='ap-southeast-1')
#SECRET_KEY = ssm.get_parameter(Name="/django-lightsail-key", WithDecryption=True)["Parameter"]["Value"]

SECRET_KEY = "1c305b704417038697acaa7eda5e2e3db063157d2d9e9344f87fef76bd7ec1e2c58348f628caa12e92ec28f1b7b1987a99077feee4cd66fd12c939ef68031384"

DEBUG = False