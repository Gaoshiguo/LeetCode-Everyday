def find_max_area(str):
	max_are=0
	left=0
	right=len(str)-1
	while left <right : 
		v=min(str[left],str[right])*(right-left)
		max_are=max(v,max_are)
		if str[left] < str[right]:
			left=left+1
		else:
			right=right-1
	return max_are


li=[1,8,6,2,5,4,8,3,7]
print(find_max_area(li))