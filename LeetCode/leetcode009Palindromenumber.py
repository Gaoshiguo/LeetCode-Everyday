def Palindromenumber(number):
	length = len(number)
	if length%2==0:
		tag=int((length/2)-1)
		left = tag  
		right = tag + 1
		while left >=0 and right <=length and number[left]==number[right]:
			left=left-1
			right=right+1
		if left > 0 or right < length:
			return False
		else:
			return True
	else:
		tag=int(length/2)
		left = tag - 1 
		right = tag + 1
		while left >=0 and right <=length and number[left]==number[right]:
			left=left-1
			right=right+1
		if left > 0 or right < length:
			return False
		else:
			return True


	


num='-13531-'

print(Palindromenumber(num))