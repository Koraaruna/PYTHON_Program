n=int(input())
l=list(map(int,input().split()))
x=int(input())
l.sort()
c=0
for i in range(n):
	if(l[i]>x):
		c=len(l[i:])
		break
print(round(c/n,2))
