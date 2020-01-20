# 题目描述
# 输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
# 
# 输入描述:
#  输入一个整数（int类型）
#
# 输出描述:
#  这个数转换成2进制后，输出1的个数


def get_count(num):
    count = 0
    while num != 0:
        if num % 2 == 1:
            count += 1
        num = int(num / 2)

    print(count)


if __name__ == '__main__':
    num = int(input())
    get_count(num)