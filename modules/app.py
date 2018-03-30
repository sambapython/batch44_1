'''
print "a=%s, b=%s, c=%s"%(a,b,c)
fun()
'''
'''
import sys
print sys.path

import f1
import f2

print "in f1: a=%s, b=%s, c=%s"%(f1.a,f1.b,f1.c)
f1.fun()
print "in f2: a=%s, b=%s, c=%s,d=%s"%(f2.a,f2.b,f2.c,f2.d)
f2.fun()
'''
'''
import f3
f3.fun()
'''
'''
import sys
sys.path.append("/home/khyaathi-python")
print sys.path
import f4
import f3
f3.fun()
'''
'''
import sys
#sys.path.append("/home/khyaathi-python")
sys.path.insert(1,"/home/khyaathi-python")
print sys.path
import f4
import f3
f3.fun()
'''
'''
import sys
import f3
sys.path.insert(1,"/home/khyaathi-python")
import f3
import f3
'''
'''
import f1
f1.fun()
f1.fun1()
'''
'''
from f1 import fun
fun()
'''

import f1
f1.fun()
print "a=",f1.a
f1.fun2()