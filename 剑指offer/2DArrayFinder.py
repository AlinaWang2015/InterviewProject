# 题目描述
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数


# [[1,2,3,4], [4,5,6,7]] 二维数组
def find(target, array):
    rows = len(array) - 1  # 行
    cols = len(array[0]) - 1  # 列
    i = rows
    j = 0
    while j <= cols and i >= 0:
        if target < array[i][j]:
            i -= 1
        elif target > array[i][j]:
            j += 1
        else:
            return True