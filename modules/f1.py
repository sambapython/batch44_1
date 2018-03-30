a=10
b=20
c=a+b
def fun():
	print "this is fun in f1 modified"
def fun1():
	print "this is fun1 in f1"

if __name__ == "__main__":
	def fun2():
		print "this is fun2 in f1"
	print "__name__:",__name__
	print __name__ == "__main__"
	print "a=%s, b=%s, c=%s"%(a,b,c)
	fun()
