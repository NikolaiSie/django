"""
Django settings for writingsite project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


import socket

if socket.gethostname() in ["L-H9CFZ33", "LAPTOP-R7NHPM8N"]:
    from .local_settings import *
else:
    from .prod_settings import *