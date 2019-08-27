import socket
import os.path
from os import path

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1237))
s.listen(5)

print ("Server is waiting")

while True:
	conn1,addr1=s.accept()
	file=str((conn1.recv(4096)).decode())
	if(os.path.exists(file)):

		print('File found	')
		f=open(file,'rb')
		l=f.read(4096)
		while(l):
			conn1.send(l)
			l=f.read(4096)
		f.close()

print("Done sending")
s.shutdown(socket.SHUT_WR)
conn1.close()

s.close()
