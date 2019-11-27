import socket
import math
import random

split_bits = {}

def isPowerOfTwo(n): 
    return (math.ceil(math.log2(n)) == math.floor(math.log2(n))); 

def bits(n):
    while n:
        b = n & (~n+1)
        yield b
        n ^= b

def generate(x):
	templist = []

	for b in bits(x):
		templist.append(b)
                

	split_bits[x]=templist



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 4549

s.connect((socket.gethostname(),port))

print("Please enter the message")

mssg = input()
data_list = list(mssg)

r = 0
while(len(data_list)+r+1<=pow(2,r)):
	r+=1

#Generating the upper limit
cnt = 0
initial_number = 3

while((cnt<len(data_list))):
	if(isPowerOfTwo(initial_number)==False):
		cnt+=1
		generate(initial_number)				
	initial_number+=1

#print(initial_number)
print(split_bits)

dummy = '-1'

total_message = []

index_cnt = 0

for i in range(initial_number):
	total_message.append(dummy)

for i in range(1,initial_number):
	if(isPowerOfTwo(i)==False):
		total_message[i]=mssg[index_cnt]
		index_cnt+=1

for i in range(1,initial_number):
	tlist = []
	if(isPowerOfTwo(i)==True):
		for keys,values in split_bits.items():
			if(i in split_bits[keys]):
				tlist.append(total_message[keys])

		cnt_ones=0		
		for j in range(len(tlist)):
			if(tlist[j]=='1'):
				cnt_ones+=1

		if(cnt_ones%2==0):
			total_message[i]='0'
		else:
			total_message[i]='1'		


string_to_be_send = ""

print(total_message)

#print(string_to_be_send)
#Generating an error
#Flip bits at random positions other than parity bits

indices = []

for i in range(1,len(total_message)+1):
	if(isPowerOfTwo(i)==False):
		indices.append(i)

#random.systemRandom()
random.shuffle(indices)

if(total_message[indices[0]]=='1'):
	total_message[indices[0]]='0'
else:
	total_message[indices[0]]='1'

for i in range(1,len(total_message)):
	string_to_be_send+=total_message[i]

print(string_to_be_send)

s.send(bytes(string_to_be_send,"utf-8"))

