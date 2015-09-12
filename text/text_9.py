'''
开始判断时while的条件错误，想着增加除数，没想到减小被除数。
'''
'''class Solution(object):
    def isPalindrome(self, x):
        print x
        n = 10
        list = []
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            while ((x % n) / (n/10)) >0 :
                list.append((x % n) / (n/10))
                n = n * 10

            print list
            print list[::-1]
            if list == list[::-1]:
                return True

'''
class Solution(object):
    def isPalindrome(self, x):
        print x
        n = 10
        list = []
        if x < 0:
            return 'False'
        elif x == 0:
            return 'True'
        else:
            while x >0 :
                list.append(x % 10)
                x = x / 10
            print list
            print list[::-1]
            if list == list[::-1]:
                return 'True'
            else:
                return 'False'

p = Solution()
p.isPalindrome(10)
