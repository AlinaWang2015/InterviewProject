# 设置两个标志位一个存储最大数一个存储次大数
# two存储次大值，one存储最大值，遍历一次数组即可，先判断是否大于one，若大于将one的
# 值给two，将num_list[i]的值给one；否则比较是否大于two，若大于直接将num_list[i]的
# 值给two；否则pass


def find_second_max(num_list):
    one, two = num_list[0], num_list[-1]
    for i in range(1, len(num_list)):
        if num_list[i] > one:
            two = one
            one = num_list[i]
        elif num_list[i] > two:
            two = num_list[i]
        else:
            pass
    print(f'第二大数字是: {two}')


if __name__ == '__main__':
    array = [2, 1, 3, 5, 4, 4, 6]
    find_second_max(array)