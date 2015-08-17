#!/usr/bin/python
import os
import sys
from pinguide_config import *

sys.path.append('.')
sys.path.append(CAFFE_DIR + '/python')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

    from pinguide_logic import RFC
    RFC.init()

    from pinguide_logic import Extractor
    Extractor.init()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
