from .base import *

SETTINGFILES_DIRS = {
    os.path.join(os.path.dirname(BASE_DIR), "settings"),
}


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        'ENGINE': 'mssql',
        'NAME':'ddrmlbjn0p67md',
        'USER': 'vqamoaupfutgjh',
        'PASSWORD': '3c2515f524d6628d0abe9d31773cc58858df558eb70acc093b9e4279ddd58f70',
        'HOST': 'ec2-3-219-19-205.compute-1.amazonaws.com',
        'PORT': '5432',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}


