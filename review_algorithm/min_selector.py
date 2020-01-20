# 输入一个数字数组，然后从数组中查找出不存在的最小的正整数
# 将输入的数组转化为set集合，因为set集合自带hash查找，时间复杂度是logn


def select_min(arr):
    temp = set(arr)
    for i in range(1, len(arr), 1):
        if i not in arr:
            print(f'不存在的最小的正整数是: {i}')
            return


if __name__ == '__main__':
    array = [int(n) for n in input().split(',')]
    select_min(array)