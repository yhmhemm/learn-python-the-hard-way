# -*- coding:utf-8 -*-
class Zipper:
    def zipString(self, iniString):
        # write code here
        length = len(iniString)
        i = 0
        s = ''
        while i < length-1:
            num = 1
            while iniString[i] == iniString[i+1]:
                print iniString[i],iniString[i+1]
                print i
                num += 1
                i += 1
            else:
            	s += iniString[i] + str(num)
                i += 1


p = Zipper()
print p.zipString('aabcccccaaa')