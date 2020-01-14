from itertools import groupby


def sort(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break


# 输入一个数字数组，然后对数组进行分块儿；最后转换成字符串
def get_format(arr):
    if not len(arr):
        print('输入数组为空')
        return

    sort(arr)
    fun = lambda x: x[1] - x[0]
    for k, g in groupby(enumerate(arr), fun):
        l1 = [j for i, j in g]
        if len(l1) > 1:
            scop = f'{min(l1)}-{max(l1)}'
        else:
            scop = l1[0]
        print(scop)


if __name__ == '__main__':
    array = [1,2,3,4,6,8,9,10]
    get_format(array)