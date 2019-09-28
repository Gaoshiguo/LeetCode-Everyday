def romanToInt(str):
	# result = " "
	# new_str=list(str)
	# new_str.reverse()
	nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
	levels = {1: "I", 4: "IV", 5: "V", 9:"IX", 10: "X", 40:"XL", 50: "L", 90:"XC", 100: "C", 400:"CD", 500: "D" , 900:"CM", 1000: "M"}  # changed
	a={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
	ans=0
	for i in range(len(str)):            
		if i<len(str)-1 and a[str[i]]<a[str[i+1]]:                
			ans-=a[str[i]]
		else:
			ans+=a[str[i]]
	return ans

#判断各个位是几，通过递减法求出各个位是几，如果是特殊值，在字典中匹配相应的value


li="CCCLXXXVI"
print(romanToInt(li))