import importlib
import sys

# For illustrative purposes.
#import tokenize
#file_path = tokenize.__file__
#module_name = tokenize.__name__

file_path = "script2.cpython-37.pyc"
module_name = "script2"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

module.myfunc()
module.myfunc("Testing from script 6.")

