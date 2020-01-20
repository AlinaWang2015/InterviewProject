# 数字反转并去重
def get_new_num(num_str):
    num_list = list(num_str)
    num_list.reverse()
    result = ''
    for num in num_list:
        if num not in result:
            result += num

    print(result)


if __name__ == '__main__':
    num_str = input()
    get_new_num(num_str)