import random
import time


def summ(list):
    base_sum = 0
    for i in range(len(list)):
        base_sum += list[i]
    return base_sum
def maxx(list):
    base_max = list[0]
    for i in range(len(list)):
        if list[i] > base_max:
            base_max = list[i]
    return base_max

def minn(list):
    base_min = list[0]
    for i in range(len(list)):
        if list[i] < base_min:
            base_min = list[i]
    return base_min

def sort_pusir(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def sort_vibor(list):
    n = len(list)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if list[j] < list[m]:
                m = j
        list[i], list[m] = list[m], list[i]
    return list

def sort_shell(list):
    n = len(list)

    # Расстояние между элементами
    gap = n // 2

    # Сортировка по разделам
    while gap > 0:
        for i in range(gap, n):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap //= 2
    return list

def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def heap_sort(list):
    n = len(list)

    # Построение кучи (перегруппируем массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]  # Перемещаем текущий корень в конец
        heapify(list, i, 0)  # Вызываем процедуру heapify на уменьшенной куче
    return list

def heapify(list, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # Левый дочерний элемент
    r = 2 * i + 2  # Правый дочерний элемент

    # Если левый дочерний элемент больше корня
    if l < n and list[l] > list[largest]:
        largest = l

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if r < n and list[r] > list[largest]:
        largest = r

    # Если самый большой элемент не корень
    if largest != i:
        list[i], list[largest] = list[largest], list[i]  # Меняем самый большой элемент с корнем
        heapify(list, n, largest)  # Рекурсивно преобразуем в двоичную кучу затронутое поддерево

def binary_search_number(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

def binary_search(arr, target):
    index = binary_search_number(arr, target)
    if index is not None:
        print(f"Элемент {target} найден под индексом {index} (Бинарный поиск)")
    else:
        print(f"Элемент {target} не найден (Бинарный поиск)")

def interpolation_search_number(arr, target):
    low = 0
    high = len(arr) - 1

    # Пока элемент не найден и диапазон поиска не пуст
    while arr[low] <= target <= arr[high] and low <= high:
        # Интерполируем позицию
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        # Если элемент найден
        if arr[pos] == target:
            return pos

        # Если целевое значение больше, чем текущий элемент, переходим к правой части массива
        if arr[pos] < target:
            low = pos + 1

        # Если целевое значение меньше, чем текущий элемент, переходим к левой части массива
        else:
            high = pos - 1

    return None

def interpolation_search(arr, target):
    index = interpolation_search_number(arr, target)
    if index is not None:
        print(f"Элемент {target} найден под индексом {index} (Интерполяционный поиск)")
    else:
        print(f"Элемент {target} не найден (Интерполяционный поиск)")



items = [random.randint(-100000, 100000) for i in range(10000000)]
start_time_sum = time.time()
summ(items)
end_time_sum = time.time()
start_time_max = time.time()
maxx(items)
end_time_max = time.time()
start_time_min = time.time()
minn(items)
end_time_min = time.time()
start_time_sort = time.time()
#print(sort_pusir(items))
#print(sort_vibor(items))
#print(sort_shell(items))
#print(quick_sort(items))
#print(merge_sort(items))
heap_sort(items)
end_time_sort = time.time()
#print(items)
start_time_bin = time.time()
binary_search(items, 45)
end_time_bin = time.time()
start_time_inter = time.time()
interpolation_search(items, 45)
end_time_inter = time.time()

print(f"Время для суммы = {end_time_sum-start_time_sum},\nВремя для максимума = {end_time_max - start_time_max},\nВремя для минимума = {end_time_min - start_time_min},\n"
      f"Время для сортировки = {end_time_sort - start_time_sort},\nВремя для бинарного поиска = {end_time_bin - start_time_bin},\nВремя для интерполяционного поиска = {end_time_inter - start_time_inter}.")


"""
N = 1000000
Элемент 45 найден под индексом 5001104 (Бинарный поиск)
Элемент 45 найден под индексом 5001097 (Интерполяционный поиск)
Время для суммы = 0.5200767517089844,
Время для максимума = 0.42647886276245117,
Время для минимума = 0.3722951412200928,
Время для сортировки = 132.63247632980347,
Время для бинарного поиска = 5.1021575927734375e-05,
Время для интерполяционного поиска = 9.059906005859375e-06.

"""