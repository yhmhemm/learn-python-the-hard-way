# -*- coding:utf-8 -*-
class Transform:
    def transformImage(self, mat, n):
        # write code here
        m = []
        num = n
        for i in range(n):
            s = []
            num = n
            while num > 0:
                s.append(mat[num-1][i])
                num -= 1
            #print s
            m.append(s)
            #print m
        return m


p = Transform()
print p.transformImage([[1,2,3],[4,5,6],[7,8,9]],3)