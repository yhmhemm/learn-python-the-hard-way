'''
方法一
先复制一个列表， 将复制得到的列表排序.sort
2个指针 一个从开头，一个从结尾
1.开头加结尾大于目标数，结尾指针减一
2.开头加结尾小于目标数，开头指针加一
3.开头加结尾等于目标数，查找远列表中的下表
'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index = []
        numtosort = num[:]; numtosort.sort()
        i = 0; j = len(numtosort) - 1
        while i < j:
            if numtosort[i] + numtosort[j] == target:
                for k in range(0,len(num)):
                    if num[k] == numtosort[i]:
                        index.append(k)
                        break
                for k in range(len(num)-1,-1,-1):
                    if num[k] == numtosort[j]:
                        index.append(k)
                        break
                index.sort()
                break
            elif numtosort[i] + numtosort[j] < target:
                i = i + 1
            elif numtosort[i] + numtosort[j] > target:
                j = j - 1

        return (index[0]+1,index[1]+1)

Solution(numbers={2, 7, 11, 15}, target=9)
'''
方法二
enumerate(num)函数返回num的下标,值.
将没一组遍历过的下标,值  存入字典.数值为键,下标为值
目标值减去当前的值 剩下的值如果在字典中,那么寻找这两个下标,并加一
要先判断的原因是:有一样值的情况,例如{2,4,4,6} 目标:8
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dictMap = {}
        for index, value in enumerate(num):
            if target - value in dictMap:
                return dictMap[target - value] + 1, index + 1
            dictMap[value] = index
