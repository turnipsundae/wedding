"""
Django settings for kevinhlau project. Fore more info, see:

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from kevinhlau.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allow all host headers
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['.elasticbeanstalk.com', '.kevinhlau.com']
