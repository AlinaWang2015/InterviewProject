# 题目描述
# 写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
#
# 输入描述:
# 第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。
#
# 输出描述:
# 输出输入字符串中含有该字符的个数。


def get_char_count(str_set, char):
    if not (str_set) or not len(char) == 1:
        print(0)
        return

    count = 0
    new_str = str_set.lower()
    new_char = char.lower()
    for set_char in new_str:
        if set_char == new_char:
            count += 1
    print(count)


if __name__ == '__main__':
    input_str = input()
    char = input()
    get_char_count(input_str, char)