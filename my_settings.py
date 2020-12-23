DATABASES = { 

    'default' : { 
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'gitomp',  
        'USER': 'root',  
        'PASSWORD': "",
        'HOST': 'localhost',   
        'PORT': '3306', 
    }

} 


SECRET_KEY    = "po4v(6tn_*6c#6bhnt&zgjaw@zdb)4(9-5zhj$1gu49%tibpvj"
JWT_ALGORITHM = "HS256"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

