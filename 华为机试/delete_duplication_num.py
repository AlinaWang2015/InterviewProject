def delete_duplication(num_count):
    num_arr = []
    for i in range(num_count):
        num_arr.append(int(input()))

    num_set = set(num_arr)

    num_lis = list(num_set)
    num_lis.sort()
    for num in num_lis:
        print(num)


if __name__ == '__main__':
    num_count = int(input())
    if num_count <= 0:
        exit()
    delete_duplication(num_count)