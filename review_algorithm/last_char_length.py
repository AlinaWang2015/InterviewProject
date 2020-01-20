# 计算字符串最后一个单词的长度，单词以空格隔开。
def get_length(input_str):
    if not len(input_str):
        print(0)

    str_arr = input_str.split(" ")
    last = str_arr[-1]
    print(len(last))


if __name__ == '__main__':
    input_str = input()
    get_length(input_str)