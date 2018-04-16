# hostname(to recognize machine in the network)
# Single machine may run with multiple services.
# available port number(to recognize service in the machine)
import socket
hostname=socket.gethostname()
port=8899
try:
	s=socket.socket()
	s.bind((hostname,port))
	s.listen(20)
	print "server runing in: %s:%s"%(hostname,port)
	print "waiting for the client request"
	#print s.accept()
	client_instance,client_info = s.accept()
	client_instance.send("Hello firefox how are you ding?")
except Exception as err:
	print err
finally:
	s.close()