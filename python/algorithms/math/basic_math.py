
from operator import length_hint


class BasicMath:

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
