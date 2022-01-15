"""
Django settings for virtual_menu project.

Generated by 'django-admin startproject' using Django 3.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
##
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%t^icwtx(^6bqz)7kch*@ifvfv60m4()g2)^1chn-2p8vihi6g'

# SECURITY WARNING: don't run with debug turned on in production!
### ----
    ### RODANDO LOCALMENTE
    ### SERVIDOR TESTE:
DEBUG = False
    ### QUANDO FOR OFICIAL
    ### COLOCAR O DEBUG ABAIXO
    
##DEBUG = config('DEBUG', cast=bool, default=False)

### UP

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    ##MEUS APLICATIVOS
    ##'whitenoise.runserver_nostatic',
    'accounts',
    'menu',
    'mesa',
    'pagamento',
    'carrinho',
    ### APLICATIVOS DO DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ##APLICATIVOS DE TERCEIROS:
        ##FORMULÁRIOS
    'crispy_forms',
    
    
       
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ## CURRENT USER
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
    
    ##
]


ROOT_URLCONF = 'virtual_menu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'virtual_menu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#Location of static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
##STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage' 

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

## AUTO COMPLETAR CAMPOS
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
## PACOTE DE FORMULÁRIOS (CRISPY FORMS)
CRISPY_TEMPLATE_PACK = 'bootstrap4'

## AUTH MODELS
AUTH_USER_MODEL = "accounts.User"
##REDIRECT 
LOGIN_REDIRECT_URL = '/cardapio/pedidos/'
LOGOUT_REDIRECT_URL = '/'


###FALTA MEDIA_URL
###COLOCAR LOO DOS PRODUTOS EM PASTA MIDIA_URL
##NECESSÁRIO AMAZON AWS
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = BASE_DIR / 'media'

##AWS_ACCESS_KEY_ID = 'AKIA5KNEFXSVOL5YTNVP'
##AWS_SECRET_ACCESS_KEY = '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'
##AWS_STORAGE_BUCKET_NAME = 'alemao'

##AWS_S3_FILE_OVERWRITE = False
##AWS_DEFAULT_ACL = None
##DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'