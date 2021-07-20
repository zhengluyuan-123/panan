from os import listdir, pathsep
from os.path import join

from jpype import startJVM,JClass,JString,shoutdownJVM
from configuration.config import get_prog_instance_dir