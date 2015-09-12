class Solution(object):
    def f(self,str1,str2):
        str3 = ''
        for i in range(min(len(str1),len(str2))):
            if str1[i] != str2[i]:
                break
            str3 += str1[i]
        return str3


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if length == 1 :
            return strs[0]
        elif length == 0:
            return None
        else:
            return reduce(self.f,strs)


p = Solution()
print p.longestCommonPrefix([])