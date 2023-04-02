
from operator import length_hint


class FundamentalMath:

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
