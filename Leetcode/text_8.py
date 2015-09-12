'''
1.去除开头的空格，数字串后面的空格及其他的不用考虑 如 123 444  中444 不用考虑
2.考虑 正负数 和负的正数 即：+（-1） 和 -（+1） 以及 +—  和 -+
3.考虑 单个 + 和负号的情况
'''
class Solution(object):
    def myAtoi(self, str):
        s = str.strip()
        length = len(s)
        #print 'length=',length
        if length == 0:
            return 0
        elif s[0] == '+' and length >1:
            for i in range(1,length):
                if s[i].isdigit() == False:
                    s = s[1:i]
                    break
        elif s[0] == '-' and length >1:
            for i in range(1,length):
                if s[i].isdigit() == False:
                    s = s[0:i]
                    break
        elif length >=1 and s[0].isdigit()==True:
            for i in range(0,length):
                if s[i].isdigit() == False:
                    s = s[0:i]
                    break
        else:
            return 0

        if len(s) ==1 and s[0]=='-':
            return 0
        if len(s)>0:
            num = int(s)
        else:
            return 0
        if num >= 2147483647:
            return 2147483647
        elif num <= -2147483648:
            return -2147483648
        else:
            return num

p = Solution()
print p.myAtoi('1')