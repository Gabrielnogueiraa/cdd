def quick_sort(arr):
    com = 0
    tro = 0

    def partition(arr, low, high):
        nonlocal com, tro
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):

            com += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                tro += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        tro += 1
        return i + 1

    def quick_sort_helper(arr, low, high):
        nonlocal com, tro
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    return tro, com

arr = [20, 15, 4, 45, 80, 11, 60]

tro, com = quick_sort(arr)
print("Quick Sort - Trocas:", tro, "Comparações:", com)
print("Sorted Array:", arr)


def insertion_sort(arr):
    com = 0
    tro = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            com += 1
            arr[j + 1] = arr[j]
            tro += 1
            j -= 1
        arr[j + 1] = key

    return tro, com


arr = [44, 12, 28, 11, 76, 91, 40]
tro, com = insertion_sort(arr)
print("Insertion Sort - Trocas:", tro, "Comparações:", com)
print("Sorted Array:", arr)


def shell_sort(arr):
    com = 0
    tro = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                com += 1
                arr[j] = arr[j - gap]

                tro += 1
                j -= gap
            arr[j] = temp
        gap //= 2

    return tro, com

arr = [46, 74, 35, 22, 92, 21, 90]
tro, com = shell_sort(arr)
print("Shell Sort - Trocas:", tro, "Comparações:", com)
print("Sorted Array:", arr)

