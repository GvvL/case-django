#coding:utf-8
"""
Django settings for Shangzhuocai project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n)c*7s@*8*m3xtg(v$1l6wm^g6h&l5y^n=akhl-0a6yxj&+p*0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

USE_TZ = True
# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'szcapp'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'Shangzhuocai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Shangzhuocai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shangzhuocai',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'PORT':'3306'
    }
}




# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
#定义 app label model
SUIT_CONFIG = {
    'ADMIN_NAME': '管理中心',
    'HEADER_DATE_FORMAT': 'l, j. F Y', # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'H:i',       # 18:42

    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,

    'SEARCH_URL': '/admin/auth/user/',
    'MENU_OPEN_FIRST_CHILD': True,#默认打开子菜单
    'MENU_ICONS': {
            'Shangzhuocai': 'icon-leaf',
            'auth': 'icon-lock',
        },
    'LIST_PER_PAGE': 10,#全局每页显示
    'MENU': (#配置菜单

        # Keep original label and models
        'Shangzhuocai',


        {'app':'szcapp','label':u'订单管理','icon':'icon-book','models':(
            {'model':'SzcOrders','label':u'订单列表','icon':'icon-book'},
        )},
        {'app':'szcapp','label':u'会员管理','icon':'icon-user','models':(
            {'model':'SzcMembers','label':u'会员列表','icon':'icon-user'},
        )},
        '-',
        {'label':u'优惠券管理','icon':'icon-tags','url':'szcapp.SzcCoupons'},
        {'app':'szcapp','label':u'收货地址管理','icon':'icon-inbox','models':(
            {'model':'SzcAddr','label':u'地址列表','icon':'icon-book'},
        )},
        '-',
        '-',
        {'app': 'auth', 'models': ('user', 'group')},
        # Custom app and model with permissions
        # {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
        #     {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
        # ]},
    )
}


