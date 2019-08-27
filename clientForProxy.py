import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),4545))
stru=input()
s.send(stru.encode())

with open(stru,'wb') as f:
	while True:
		data=s.recv(4096)
		if not data:
			break
		f.write(data)


print("File recieved")
s.close()
