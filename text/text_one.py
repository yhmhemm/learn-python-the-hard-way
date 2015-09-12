'''
����һ
�ȸ���һ���б� �����Ƶõ����б�����.sort
2��ָ�� һ���ӿ�ͷ��һ���ӽ�β
1.��ͷ�ӽ�β����Ŀ��������βָ���һ
2.��ͷ�ӽ�βС��Ŀ��������ͷָ���һ
3.��ͷ�ӽ�β����Ŀ����������Զ�б��е��±�
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
������
enumerate(num)��������num���±�,ֵ.
��ûһ����������±�,ֵ  �����ֵ�.��ֵΪ��,�±�Ϊֵ
Ŀ��ֵ��ȥ��ǰ��ֵ ʣ�µ�ֵ������ֵ���,��ôѰ���������±�,����һ
Ҫ���жϵ�ԭ����:��һ��ֵ�����,����{2,4,4,6} Ŀ��:8
'''
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dictMap = {}
        for index, value in enumerate(num):
            if target - value in dictMap:
                return dictMap[target - value] + 1, index + 1
            dictMap[value] = index
