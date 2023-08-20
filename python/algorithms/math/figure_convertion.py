import math


class NFigureConversion:
        
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