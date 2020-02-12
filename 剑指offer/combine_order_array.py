# 实现两个有序数组合并为一个有序数组

# 临时变量i，j分别标识2个数组的起始位置。临时数组temp，用变量k表示其填充位置
# a[i]与a[j]比较大小，依次填充到temp
# 最后判断哪个数组还有剩余start与end，然后将剩余部分之间加入到temp
# temp整体拷贝到原数组a中


def merge(a, b):
    """
    合并2个有序数组，默认a，b都是从小到大的有序数组
    """
    # 1.临时变量
    i, j = 0, 0  # 分别标记2个数组的起始位置
    na, nb = len(a), len(b)  # 分别标记2个数组的长度
    temp = []  # 临时存放空间
    # 2.只要2个数组不为空：比较大小a[i]a[j]，依次填入temp
    while i <= na - 1 and j <= nb - 1:
        if a[i] <= b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1
    # 3.判断哪个数组还有剩余
    if i <= na - 1:
        start = i
        end = na - 1
        # 4.将剩余部分添加到temp中
        temp.extend(a[start:end + 1])
    else:
        start = j
        end = nb - 1
        temp.extend(b[start:end + 1])
    # 5.返回合并的新数组
    return temp


if __name__ == '__main__':
    a = [1, 2, 4, 6, 9]
    b = [5, 8, 10, 22]
    mergeArr = merge(a, b)
