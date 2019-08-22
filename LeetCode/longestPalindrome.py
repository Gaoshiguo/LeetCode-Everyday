def longestPalindrome(s):
        if len(s)==0:
        	return "字符串不合法，请输入有效字符串，长度至少为1"
        

        longest_palindrome = 1
        longest_palindrome_str = s[0]
        length=len(s)
        for i in range(length):
            palindrome_odd, odd_len = spread(s, length, i, i)
            palindrome_even, even_len = spread(s, length, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > longest_palindrome:
                longest_palindrome = len(cur_max_sub)
                longest_palindrome_str = cur_max_sub

        return longest_palindrome_str
def spread(str,length,left,right):
    while left >= 0 and right < length and str[left] == str[right]:
        left -= 1
        right += 1
    return str[left + 1:right], right - left - 1

num_1="asdadqfwegfgradsadwd"
print(longestPalindrome(num_1))