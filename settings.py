# Django settings for jsdh project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

# DH data
P = 114454352258618336192858445991095376892568036802441830957445273627422796190483L
# From wikipedia
#  The order of G should have a large prime factor to prevent use
#  of the Pohlig–Hellman algorithm to obtain a or b. For this reason,
#  a Sophie Germain prime q is sometimes used to calculate p = 2q + 1,
#  called a safe prime, since the order of G is then only divisible
#  by 2 and q. g is then sometimes chosen to generate the order q
#  subgroup of G, rather than G, so that the Legendre symbol of g^a
#  never reveals the low order bit of a.
G = 5

MANAGERS = ADMINS

CACHE_BACKEND = 'memcached://10.135.2.132:11211;10.135.2.133:11211;10.135.2.134:11211;10.135.2.135:11211/'
CACHE_MIDDLEWARE_KEY_PREFIX = 'jsdh:'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite'
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$4a3f7+j-k%o7vu!#!3d@#*o9^tkii9(-(ja4hknn*vcxg6)t1'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
)

INSTALLED_APPS = (
#    'django.contrib.auth',
    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
)
