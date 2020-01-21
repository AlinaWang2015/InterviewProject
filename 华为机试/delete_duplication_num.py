# 输入描述:
# 输入多行，先输入随机整数的个数，再输入相应个数的整数
#
# 输出描述:
# 返回多行，处理后的结果


import sys

while True:
    try:
        num_count = int(input())
        num_arr = []
        for i in range(0, num_count):
            num_arr.append(int(sys.stdin.readline()))

        num_set = set(num_arr)
        num_lis = list(num_set)
        sorted(num_lis)

        for num in num_lis:
            print(num)
    except:
        break

