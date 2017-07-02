"""
WSGI config for sclm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

status = '200 OK'

output = 'sys.path = %s\n' % repr(sys.path)
output += 'sys.version = %s\n' % repr(sys.version)
output += 'sys.prefix = %s\n' % repr(sys.prefix)

print output

sys.path = ['/home/liujie/sclm/extra_apps', '/home/liujie/sclm', '/usr/local/lib/python2.7/dist-packages/setuptools-18.1-py2.7.egg', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/home/liujie/.local/lib/python2.7/site-packages', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/python2.7/dist-packages/ubuntu-kylin-sso-client', '/usr/lib/python2.7/dist-packages/ubuntu-sso-client']

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sclm.settings")

application = get_wsgi_application()
