def decryptPassword(s):
    # Write your code here
	b=""
	i=0
	l=[]
	while(i<len(s)-1):
		if(s[i+1].islower() and s[i].isupper()):
			b+=s[i+1]
			b+=s[i]
			i+=3
		elif(s[i].isdigit() and s[i]!='0'):
			l.append(s[i])
			i+=1
		elif(s[i]=='0'):
			b+=l[-1]
			del l[-1]
			i+=1
		else:
			b+=s[i]
			i+=1
	return b
s="51Pa*0Lp*0e"
print(decryptPassword(s))
