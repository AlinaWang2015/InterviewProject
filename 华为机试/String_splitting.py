# •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。


import sys

a = sys.stdin.readline().replace('\n', '')
b = sys.stdin.readline().replace('\n', '')
c = [a[i:i + 8] for i in range(0, len(a), 8)]
d = [b[i:i + 8] for i in range(0, len(b), 8)]
z = c + d
print(c)
print(d)
print(z)
for i in z:
    if len(i) < 8:
        x = i + (8 - len(i)) * '0'
        print(x)
    else:
        print(i)

