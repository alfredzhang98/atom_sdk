
from operator import length_hint


class SumUtils:

    #暴力解法
    def twoSum(array, target):
        n = len(array)
        for i in range(n):
            for j in range(i + 1, n):
                if array[i] + array[j] == target:
                    return [i, j]
        return []

    def threeSum(array):
        #避免重复答案做准备
        array.sort()
        result_array = []
        lengthGet = len(array)

        # 从左向右进行搜索 left头指针
        for left in range(lengthGet):
            # 从左往右滑动的时候避免相同的数值出现
            if left > 0 and array[left] == array[left-1]:
                continue
            #当前left指针的下一个数值开始
            target= left+1
            #right尾指针
            right = lengthGet - 1
            while target < right:
                result = array[left] + array[target] + array[right]
                if  result < 0:
                    # 如果和小于0，目标增大
                    target += 1  
                elif result > 0:
                    # 如果和小于0，右边指针需要增大
                    right -= 1
                else:
                    result_array.append([array[left], array[target], array[right]])
                    #剔除重复的数值
                    while target < right and array[target] == array[target+1]:
                        target += 1
                    while target < right and array[right] == array[right-1]:
                        right -= 1
                    #准备下一个枚举过程
                    target = target+1
                    right = right-1

        return result_array