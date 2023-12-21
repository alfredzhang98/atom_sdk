
from operator import length_hint


class BasicMath:

    def transDecimaltoFractional(input):
        str_bin = (bin(input))
        str_bin =  str_bin [2:]
        length1 = len(str_bin)
        if length1 % 4 != 0:
            str_bin = str_bin.zfill(4 * (int(length1 / 4) + 1))
        # print("bin: " + str_bin)

        length2 = len(str_bin)
        shift = length2 - 1
        # print("shift: " + str(shift))

        for i in range(length2):
            if i == 0:
                if str_bin[i] == '1':
                    num = -1
                else:
                    num = 0
            else:
                num = num + (2 ** (length2 - i - 1 - shift)) * int(str_bin[i])

        return num

    # 斐波那契数列是一个数列，每一项都是前两项之和。在此代码中，计算的结果需要对一个特定的模进行取余操作，以防止数值溢出。
    def fibonacci(value):
            #取模
            MODEL = 10 ** 9 + 7
            if value < 2:
                return value
            #赋初值
            a, b, now = 0, 0, 1

            #递推
            for i in range(2, value + 1):
                a = b
                b = now
                now = (a + b) % MODEL
            return now
