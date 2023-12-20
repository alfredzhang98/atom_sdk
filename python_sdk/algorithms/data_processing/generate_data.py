import math
import random


class GenerateData:
    # 根据seed 
    def generateArrayRandomBySeed(min_value, max_value, num, seed):
        random.seed(seed)  # 设置随机数种子
        data_range = max_value - min_value + 1
        
        if data_range < num:
            raise ValueError("The data range is less than the number of unique values required.")
        
        unique_values = list(range(min_value, max_value + 1))
        # Randomly upset the order
        random.shuffle(unique_values)
        
        random_data = unique_values[:num]
        return random_data