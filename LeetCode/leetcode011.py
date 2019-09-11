def intToRoman(num):
	result = " "
	nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
	levels = {1: "I", 4: "IV", 5: "V", 9:"IX", 10: "X", 40:"XL", 50: "L", 90:"XC", 100: "C", 400:"CD", 500: "D" , 900:"CM", 1000: "M"}  # changed
	i = 0
	while num>0:
		if num >= nums[i]:
			result += levels[nums[i]]
			num -= nums[i]
		else:
			i += 1
	return result



#判断各个位是几，通过递减法求出各个位是几，如果是特殊值，在字典中匹配相应的value


li=1994
print(intToRoman(li))