# 基本的求最大公约数
def get_max_common_factor(a, b):
    if a< b:
        a, b = b, a

    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    print(b)


# 优化后的递归法求最大公约数
def get_common_factor(a, b):
    if b == 0:
        print(a)
    else:
        get_common_factor(b, a % b)


# 最小公倍数
def get_min(a, b):
    return int(a * b / get_common_factor(a, b))


if __name__ == '__main__':
    arr = [int(n) for n in input().split(',')]
    get_common_factor(arr[0], arr[1])