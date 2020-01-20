# 题目描述
# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。


def fun(num_str):
    num_arr = num_str.split(".")
    index = num_str.index('.') + 1
    sub_num = int(num_str[index])
    if sub_num < 5:
        print(num_arr[0])
    else:
        print(int(num_arr[0]) + 1)


if __name__ == '__main__':
    num = input()
    # 一句话实现
    print(round(float(num)))
    fun(num)