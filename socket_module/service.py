# hostname(to recognize machine in the network)
# Single machine may run with multiple services.
# available port number(to recognize service in the machine)
import socket
hostname=socket.gethostname()
port=8899
def is_prime(number):
	if number<2:
		return False
	if number==2:
		return True
	for i in range(2,number):
		if number%i==0:
			return False
	else:
		return True 
try:
	s=socket.socket()
	s.bind((hostname,port))
	while True:
		s.listen(20)
		print "server runing in: %s:%s"%(hostname,port)
		print "waiting for the client request"
		#print s.accept()
		client_instance,client_info = s.accept()
		client_instance.send("Hello firefox how are you ding?")
		client_number=client_instance.recv(10)
		result = is_prime(int(client_number))
		client_instance.send(str(result))

except Exception as err:
	print err
finally:
	s.close()