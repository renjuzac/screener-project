import os

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "screener.settings")
django.setup()

from screentools.stocks import util

util.update_allreports()
