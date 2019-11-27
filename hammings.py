import socket
import math
import random

port = 4549

split_bits = {}
#Hamming Code Detection 
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
s.bind(('0.0.0.0',port))

s.listen(5)

conn,addr = s.accept()

data = conn.recv(1024)

retrieve = data.decode("utf-8")

message_list = list(retrieve)
second_list = list(retrieve)

print("The message from client is")
print(retrieve)

recompute = ""

for i in range(len(message_list)):
	if(isPowerOfTwo(i+1)==False):
		recompute+=message_list[i]

print("The string after removing parity it")
print(recompute)

recompute_list = list(recompute)

r = 0
while(len(recompute_list)+r+1<=pow(2,r)):
	r+=1

cnt = 0
initial_number = 3

while((cnt<len(recompute_list))):
	if(isPowerOfTwo(initial_number)==False):
		cnt+=1
		generate(initial_number)					
	initial_number+=1

print(split_bits)

dummy = -1

total_message = []

index_cnt = 0

for i in range(initial_number):
	total_message.append(dummy)

for i in range(1,initial_number):
	if(isPowerOfTwo(i)==False):
		total_message[i]=recompute[index_cnt]
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
for i in range(1,len(total_message)):
	string_to_be_send+=total_message[i]

#Store Parity of initial string
parity_first = []
parity_second= []

for i in range(0,len(second_list)):
	if(isPowerOfTwo(i+1)):
		parity_first.append(int(second_list[i]))

for i in range(1,len(total_message)+1):
	if(isPowerOfTwo(i)):
		parity_second.append(int(total_message[i]))


print(parity_first)
print(parity_second)


parity_final = []
#Take the XOR of parity bits from the received and generated string.

for i in range(len(parity_first)):
	x = parity_first[i]^parity_second[i]
	parity_final.append(x)


parity_final.reverse()

final_bit_string = ""

for i in range(len(parity_final)):
	final_bit_string+=str(parity_final[i])

position_to_be_corrected = int(final_bit_string,2)

print(position_to_be_corrected)
#print(string_to_be_send)
if(second_list[position_to_be_corrected-1]=='0'):
	second_list[position_to_be_corrected-1]='1'
else:
	second_list[position_to_be_corrected-1]='0'

final_string = ""

print("The Error is corrected and the string is")
for i in range(len(second_list)):
	final_string+=second_list[i]

print(final_string)

conn.close()
