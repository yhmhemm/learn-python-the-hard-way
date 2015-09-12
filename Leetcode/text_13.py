class Solution(object):
    def romanToInt(self, s):
        num_dict={ "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        length = len(s)
        num = 0
        i = 0
        while i < length-1:
            if num_dict[s[i]] >= num_dict[s[i+1]]:
                    num += num_dict[s[i]]
                    i += 1
                    print 'num:',num,'i:',i
            else :
                num -= num_dict[s[i]]
                i += 1
                print 'num:',num,'i:',i
        return num + num_dict[s[length-1]]

p = Solution()
print p.romanToInt("MDCXCV")