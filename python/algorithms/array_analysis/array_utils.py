
from operator import length_hint


# 数组内部一定数量的元组，根据target结果进行求和，返回结果
class ArraySum:

    # 一个整数数组和一个目标值，函数通过在数组中找到两个数，使得它们的和等于目标值，并返回这两个数在数组中的索引
    # 暴力解法
    def twoSum(array, target):
        n = len(array)
        for i in range(n):
            for j in range(i + 1, n):
                if array[i] + array[j] == target:
                    return [i, j]
        return []

    # 找到数组中所有满足三个数之和为0的组合，将这些组合以列表的形式返回。
    # 代码通过排序和双指针法，遍历数组并找出所有满足三数之和为0的组合，并且去重处理，最后返回这些组合的列表。
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