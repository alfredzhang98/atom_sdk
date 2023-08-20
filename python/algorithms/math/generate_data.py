import math
import random


class GenerateData:

    # 根据seed 
    def generateArrayRandomBySeed(min_value, max_value, num, seed):
        random.seed(seed)  # 设置随机数种子
        data_range = max_value - min_value + 1
        
        if data_range < num:
            raise ValueError("数据范围小于所需的唯一值数量。")
        
        unique_values = list(range(min_value, max_value + 1))
        random.shuffle(unique_values)  # 随机打乱顺序
        
        random_data = unique_values[:num]  # 取前num个元素作为随机数据
        return random_data