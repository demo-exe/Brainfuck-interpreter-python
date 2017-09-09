from sys import path
from os.path import dirname

# Add project top-level dir to patch
# relative imports are disabled in python 3
# so we need this hack to import Core 
path.append(dirname(path[0]))