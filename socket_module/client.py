import socket
host="khyaathipython"
port=8899
try:
	s=socket.socket()
	s.connect((host,port))
	ack=s.recv(1024)
	print "ack=",ack
	number=raw_input("enter number:")
	s.send(number)
	resp=s.recv(10)
	print "response=",resp
except Exception as err:
	print err
finally:
	s.close()
