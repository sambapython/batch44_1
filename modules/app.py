'''
print "a=%s, b=%s, c=%s"%(a,b,c)
fun()
'''

import f1
import f2
print "in f1: a=%s, b=%s, c=%s"%(f1.a,f1.b,f1.c)
f1.fun()
print "in f2: a=%s, b=%s, c=%s,d=%s"%(f2.a,f2.b,f2.c,f2.d)
f2.fun()
