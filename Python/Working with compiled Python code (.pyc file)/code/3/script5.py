"""$ cat /tmp/my_module.py
def yayfunctions(a):
    print a
$ python -m compileall /tmp/my_module.py
$ ls /tmp/my_module.py*
my_module.py   my_module.pyc
$ python
>>> import imp
>>> my_module = imp.load_compiled("my_module", "/tmp/my_module.pyc")
>>> my_module.yayfunctions('a')
a"""


import imp
my_module = imp.load_compiled("script2", "script2.cpython-37.pyc")
my_module.myfunc('Testing script 5.')
