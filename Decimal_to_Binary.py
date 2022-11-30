#Conversion from decimal to binary


n=int(input())
s=""
while(n>=1):
	s=str(n%2)+s
	n=n//2
print(s)
	

