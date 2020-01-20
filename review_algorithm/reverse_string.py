# 描述：
#
# 输入一个整数，将这个整数以字符串的形式逆序输出
#
# 程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001


def get_new_str(num_str):
    if not len(num_str):
        return
    if len(num_str) == 1:
        print(num_str)

    new_str = ''
    for char in range(len(num_str) - 1, -1, -1):
        new_str = new_str + char

    print(new_str)


if __name__ == '__main__':
    num_str = input()
    # 一句话实现
    print(num_str[::-1])
    get_new_str(num_str)