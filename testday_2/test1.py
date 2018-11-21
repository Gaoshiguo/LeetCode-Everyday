#两种方法实现首字母大写
def upper_first(s):
	return s[0].upper()+s[1:].lower()
print(list(map(upper_first,['shams','kevindrant','james','kobebrant'])))
def upper_first1(s):
	return s.capitalize()
print(list(map(upper_first,['shams','kevindrant','james','kobebrant'])))