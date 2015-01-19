#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/admin/python/")

from wePredictAPI import app as application
application.secret_key = 'Add your secret key'
