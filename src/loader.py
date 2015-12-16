

do_nothing_script_name = 'gaebuildoutdemo_app_do_nothing'

import sys
import os

from imp import load_source
from copy import copy

# Grab a copy of the original sys.path
calling_sys_path = copy(sys.path)

# Work out the do_nothing_script_path
loader_py_path = os.path.realpath(__file__)
loader_py_path = os.path.abspath(loader_py_path)
app_dir = os.path.dirname(loader_py_path)
do_nothing_script_path = os.path.join(app_dir, 'bin', do_nothing_script_name)

# Load our script if it were a module, this will alter the sys.path to
# that of our egg.
load_source(do_nothing_script_name, do_nothing_script_path)

# Prepend the original calling sys.path so we ensure that
# we use GAE paths before ours.
sys.path =  sys.path + calling_sys_path

# Load application
from pyramid.paster import get_app
application = get_app('gae.ini', 'main')
