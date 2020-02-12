# 在一个长度为n的数组里，所有数字都是0到n-1的范围之内，数组中某些数字是重复的，但是不知道哪几个数字重复了，重复的数字出现了几
# 次，请找出数组中任务一个重复的数字。


# 解决办法一：先排序，然后排序后的数组中，从头到尾扫描一遍数组就可以了。但是这样需要的时间复杂度是o(nlogn)

# 解决办法二：使用set结构或hash结构


# 这种是不改变原数组的情况
def use_map(numbers):
    """
    使用哈希表结构
    :param numbers:
    :return:
    """
    num_map = dict()
    for number in numbers:
        if number in num_map:
            print(number)
        else:
            num_map[number] = True


def use_set(numbers):
    """
    使用set结构
    :param numbers:
    :return:
    """
    num_set = set()
    for number in numbers:
        if number in num_set:
            print(number)
        else:
            num_set.add(number)


def use_sort(numbers):
    """
    排序后查找
    :param numbers:
    :return:
    """
    numbers = sorted(numbers)
    print(numbers)
    for index, number in enumerate(numbers):
        if index != number:
            continue
        if number == numbers[number]:
            print(number)
        else:
            numbers[index], numbers[number] = numbers[number], numbers[index]


if __name__ == '__main__':
    numbers = [2, 3, 1, 0, 2, 5, 3]
    use_map(numbers)
    use_set(numbers)
    use_sort(numbers)
