from binary_tree import BTree, BitTreeUtils

arrayGet = BitTreeUtils.generateBitTree(10)
print("*****arrayGet*****")
print(arrayGet)

level_all_order = BitTreeUtils.getLevelAllArray(arrayGet)
print("*****level_all_order*****")
print(level_all_order)

treeGet = BTree()
mainTree = BitTreeUtils.createBTreeByList(level_all_order)
result = treeGet.binaryTreePaths(mainTree)
print(result)
