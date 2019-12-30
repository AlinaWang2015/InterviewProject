def quick_sort(array, left, right):
    if left < right:
        pivot_position = partition_array(array, left, right)
        quick_sort(array, left, pivot_position - 1)
        quick_sort(array, pivot_position + 1, right)


def partition_array(array, left, right):
    pivot_num = array[right]
    min_position = left - 1
    for j in range(left, right):
        if array[j] <= pivot_num:
            min_position += 1
            array[min_position], array[j] = array[j], array[min_position]

    array[min_position + 1], array[right] = array[right], array[min_position + 1]
    return min_position + 1


if __name__ == "__main__":
    array = [2, 1, 3, 5, 4]
    quick_sort(array, 0, 4)
    print(array)