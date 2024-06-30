import marshal
s = open('script2.cpython-37.pyc', 'rb')
s.seek(12)  # go past first eight bytes # While I don't have much confidence, but Python 3.3+ seems to requires another 4 bytes in a head magic munbers, so s.seek(8) needs to be s.seek(12).

code_obj = marshal.load(s)
exec(code_obj)
myfunc()
myfunc("Testing from script4")