def bubble_algorithm(array):
    for i in range(len(array) - 1):
        flag = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True

        if not flag:
            return array

    return array


if __name__ == "__main__":
    array = [2, 1, 3, 5, 4]
    bubble_algorithm(array)
    print(array)
