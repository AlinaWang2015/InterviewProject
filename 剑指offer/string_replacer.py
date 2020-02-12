# 题目描述
# 请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
# 主要思路：1.用python字符串的replace方法。
# 　　　　　2.对空格split得到list，用‘%20’连接（join）这个list
# 　　　　　3.由于替换空格后，字符串长度需要增大。先扫描空格个数，计算字符串应有的长度，
#            从后向前一个个字符复制（需要两个指针）。这样避免了替换空格后，需要移动的操作。


class Solution:

# 复杂度：O(N^2)
    def replace_space_normal(self, s):
        return s.replace(' ', '%20')

# 复杂度：O(N)
    def replace_space(self, s):
        p1 = len(s) - 1
        res = list(s)
        n = s.count(' ')
        res += [0] * n * 2
        p2 = len(res) - 1
        while p1 != p2:
            if res[p1] == ' ':
                res[p2] = '0'
                res[p2 - 1] = '2'
                res[p2 - 2] = '%'
                p2 -= 3
            else:
                res[p2] = res[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(res)

