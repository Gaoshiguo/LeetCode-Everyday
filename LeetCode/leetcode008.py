def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

str="55654 with words -124554564664564"
arr=[]
tag = 0
for i in range(0,len(str)-1):
	if is_number(str[i]) == False and str[i] !="-":
		pass
	elif is_number(str[i+1]) == False:
		arr.append(str[i])
		break
	else:
		arr.append(str[i])	
if is_number(str[len(str)-1]) == True:
	arr.append(str[(len(str))-1])


s=''.join(arr)
if tag==0:
	s=s
if tag==1:
	s=s*(-1)

lin = int(s)

if lin <= (2**31)-1 and lin >= -(2**31)+1:
 	print(lin)
elif tag==0:
 	print("超出正数表示范围溢出") 
elif tag==1:
	print("超出负数表示范围溢出")
