def sumlist(number_1, number_2):
	length=len(number_1) if len(number_1)<=len(number_2) else len(number_2)
	result=[]
	for i in range(0,length):
		result.append(number_1[i]+number_2[i])
	print(result)
	if len(number_1)<len(number_2):
		for i in range(len(number_1),len(number_2)):
			result.append(number_2[i])
	else:
		for i in range(len(number_2),len(number_1)):
			result.append(number_1[i])
	print(result)		
	for i in range(0,len(result)-1):
	  	if result[i]>=10:
	  		result[i]=(result[i])%10
	  		result[i+1]=result[i+1]+1
	  	else:
	  		result[i]=result[i]
	if result[len(result)-1]>=10:
		result[len(result)-1]=result[len(result)-1]%10
		result.append(1)
	else:
		result[len(result)-1]=result[len(result)-1]
	print(result)

number_1=[2,5,8] 
number_2=[7,5,6] 
print(sumlist(number_1,number_2))


