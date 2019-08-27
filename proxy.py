import socket
import os.path
from os import path

port_c=4545
port_s=1237

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),port_c))
s.listen(5)

while True:
	conn,addr=s.accept()
	file=str((conn.recv(4096)).decode())
	if(os.path.exists(file)):
		print("File found in proxy")
		f=open(file,'rb')
		l=f.read(4096)
		while(l):
			conn.send(l)
			l=f.read(4096)
		f.close()
		print("Done sending from proxy")
		conn.close()

	else:
		s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s1.connect((socket.gethostname(),port_s))
		print("Connected to main server")
		s1.send(file.encode())
		with open(file,'wb') as f:
			# while True:
			data=s1.recv(4096)
			if not data:
				break
			f.write(data)	
		print("File recieved at proxy")
		s1.close()
		if(os.path.exists(file)):
			print("File found")
			f=open(file,'rb')
			l=f.read(4096)
			while(l):
				conn.send(l)
				l=f.read(4096)
			f.close()
		print("Done sending to client")
		conn.close()
s.close()
