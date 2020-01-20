# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def divide2prime(num):
    for i in range(2, num):
        if is_prime(i):
            while True:
                if (num % i == 0) and (i <= num):
                    num /= i
                    print(str(i), end=' ')
                else:
                    break


def find_factors(num):
    if num <= 0:
        return

    prime = True
    for i in range(2, int(num ** 0.5 + 2)):
        if num % i == 0:
            prime = False
            print(str(i), end=' ')
            find_factors(int(num / i))
            break

    if prime:
        print(str(num), end=' ')

    return


if __name__ == '__main__':
    num = int(input())
    # 这个方法效率太慢了
    # divide2prime(num)
    find_factors(num)