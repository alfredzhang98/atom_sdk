import random as ran

# 二叉树类
class BTree(object):

    # 初始化
    def __init__(self, data=None, left=None, right=None):
        self.data = data    # 数据
        self.left = left    # 左子树
        self.right = right  # 右子树

    #数组子叶到根的所有路径
    def binaryTreePaths(self, tree):
        #判断树情况
        if not tree:
            return []
        #判断子叶情况
        if not tree.left and not tree.right:
            return [str(tree.data)]
        reslut = []
        #递归寻找连路上的所有子叶
        if tree.left:
            for i in self.binaryTreePaths(tree.left):
                reslut.append(str(tree.data) + '->' + i)
        if tree.right:
            for i in self.binaryTreePaths(tree.right):
                reslut.append(str(tree.data) + '->' + i)
        return reslut  

class BitTreeUtils:

    #直接生成数组
    def generateBitTree(nodeNumSet):
        nodeNum = 1
        treeArr = [ran.randint(-100,100)]
        while nodeNum < nodeNumSet:
            left_num = ran.random()
            right_num = ran.random()
            left_or_right = ran.random()
            #该节点是否有左分枝
            if left_num > 0.2:
                left_num = 1
            else:
                left_num = 0
            #该节点是否有右分枝
            if right_num > 0.2:
                right_num = 1
            else:
                right_num = 0
            #判断节点是否满足足够数量
            if right_num == 0 and left_num == 0 and nodeNum <= nodeNumSet:
                if left_or_right > 0.5:
                    #choose left
                    left_num = 1
                else:
                    #choose right
                    right_num = 1

            if left_num == 1:
                nodeNum += 1
                if(nodeNum <= nodeNumSet):
                    treeArr.append(ran.randint(-100,100))
            else:
                treeArr.append("*")

            if right_num == 1:
                nodeNum += 1
                if(nodeNum <= nodeNumSet):
                    treeArr.append(ran.randint(-100,100))
            else:
                treeArr.append("*")

        return treeArr

    #判断生成数据的层数和每层的节点情况
    def getLevelArray(array):
        #判断数组
        if not array:
            return
        i = 1
        j = 0
        level_order = []
        node_num = 1
        #根数据赋值
        level_order.append(array[0:1])
        #循环分层数据
        while (i + node_num * 2) < len(array):
            mid_array = array[i:i + node_num * 2]
            i += len(mid_array)
            for j in range(len(mid_array)-1,-1,-1):
                if mid_array[j] == '*':
                    mid_array.pop(j)
            node_num = len(mid_array)
            level_order.append(mid_array)
        #剩余数据
        final_array = array[i:]
        for j in range(len(final_array)-1,-1,-1):
            if final_array[j] == '*':
                final_array.pop(j)
        level_order.append(final_array)
        #输出
        # print(level_order)
        # print(len(level_order))
        return level_order

    def getLevelAllArray(array):
        #判断数组
        if not array:
            return
        i = 1
        j = 0
        level_all_order = []
        node_num = 1
        #根数据赋值
        level_all_order.append(array[0:1])
        #循环分层数据
        while (i + node_num * 2) < len(array):
            mid_array = array[i:i + node_num * 2]
            i += len(mid_array)
            count = 0
            for j in range(len(mid_array)-1,-1,-1):
                if mid_array[j] == '*':
                    count += 1
            node_num = len(mid_array) - count
            level_all_order.append(mid_array)
        #剩余数据
        final_array = array[i:]
        level_all_order.append(final_array)
        #输出
        return level_all_order

    # 利用数组构造二叉树
    def createBTreeByList(level_all_order):

        # 节点迭代函数
        # bTree_part: 这一层所有的节点组成的列表
        # forword_level: 上一层所有数据
        # now_level: 这一层所有数据
        def createBTreeStep(bTree_part, forword_level, now_level):
            bTree_list_result = []
            i = 0
            count = 0
            for elements in forword_level:
                if elements == '*':
                    continue
                else:
                    root = BTree(elements)
                    if 2*i < len(now_level) :
                        if now_level[2*i] != '*':
                            # print(now_level[2*i])
                            root.left = bTree_part[count]
                            count += 1
                    if 2*i+1 < len(now_level) :
                        if now_level[2*i + 1] != '*' :
                            # print(now_level[2*i + 1])
                            root.right = bTree_part[count]
                            count += 1
                    bTree_list_result.append(root)
                    i += 1
            return bTree_list_result

        # 如果只有一个节点
        if len(level_all_order) == 1:
            #创建只有根节点的树
            return BTree(level_all_order[0][0])
        else:
            # 创建节点对象列表
            bTree_list = []
            for elements in level_all_order[-1]:
                if elements != '*':
                    bTree_list.append(BTree(elements))
            # 从下往上，逐层创建二叉树
            for i in range(len(level_all_order)-2, -1, -1):
                # print (level_all_order[i])
                # print (level_all_order[i+1])
                bTree_list = createBTreeStep(bTree_list, level_all_order[i], level_all_order[i+1])
            return bTree_list[0]