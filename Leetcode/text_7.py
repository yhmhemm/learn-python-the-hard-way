'''第一次的代码,用了while循环，其实很多余'''
class Solution(object):

    def reverse(self, x):
        list = str(x)
        num = ''
        length = len(list)
        if x > 0:
            while length>0:
                num += list[length-1]
                length-= 1
        elif x < 0:
            num += list[0]
            while length-1>0:
                num += list[length-1]
                length-= 1
        else:
            num = 0
        if -2147483648<=int(num) <= 2147483647:
            return int(num)
        else:
            return 0

'''第二次的代码，用了切片 '''
class Solution(object):

    def reverse(self, x):
        list = str(x)
        num = ''
        length = len(list)
        if x > 0:
            num = list[::-1]
        elif x < 0:
            num += list[0]
            num += list[:0:-1]
        else:
            num = 0
        if -2147483648<=int(num) <= 2147483647:
            return int(num)
        else:
            return 0


