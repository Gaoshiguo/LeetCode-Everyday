import re
def myAtoi(str): 
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

s="-4139 with words"
print(myAtoi(s))