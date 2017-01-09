# Tells PythonAnywhere where the web app lives and what de Django settings file name is
import os
import sys
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

path = '/home/enzotrompeneers/secundaire-school' 
if path not in sys.path:
    sys.path.append(path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "secundaireSchool.settings")
application = StaticFilesHandler(get_wsgi_application())

#os.environ['DJANGO_SETTINGS_MODULE'] = 'secundaireSchool.settings'
#application = get_wsgi_application()
