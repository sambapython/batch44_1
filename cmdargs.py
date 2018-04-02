# python cmdargs.py 100 200
# can get those 100 and 200 using sys.argv
'''
import sys
print sys.argv
'''
'''
import sys
args=sys.argv
number1 = int(args[1])
number2 = int(args[2])
print number2+number1
'''
import sys
args=sys.argv[1:]
print args
args_int = map(int,args)
print args_int
print sum(args_int)

