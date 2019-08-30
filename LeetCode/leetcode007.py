import re
class Solution:
    def reverse(self, x: int) -> int:
        st = str(abs(x))
        st = ''.join(re.findall('(.*)0*',st))
        st=list(st)
        st.reverse()
        tag = 1 if x >= 0 else -1
        res = int(''.join(st[0:len(st)]))
        res = res if res  >= -  2147483648 and res  <= 2147483647 else 0
        return res*tag
if __name__ == "__main__":
    s = Solution()
    res=s.reverse(-123456)
    print(res)

