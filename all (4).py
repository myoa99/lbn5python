# Исходный массив 
arr = [3.5, -7.2, 0, 4.1, -1.3, 2.8, 0, -5.6, 6.7]

print("Исходный массив:", arr)

# Максимальный по модулю элемент
max_abs = max(arr, key=abs)
print("Максимальный по модулю элемент:", max_abs)

# Сумма элементов между первым и вторым положительными элементами
positive_indices = [i for i, x in enumerate(arr) if x > 0]  # Индексы положительных элементов

if len(positive_indices) < 2:
    print("В массиве меньше двух положительных элементов — сумма не вычисляется.")
else:
    first_pos = positive_indices[0]  # Индекс первого положительного элемента
    second_pos = positive_indices[1]  # Индекс второго положительного элемента

    # Сумма элементов СТРОГО между ними (не включая сами положительные элементы)
    if first_pos + 1 < second_pos:  # Проверяем, есть ли элементы между ними
        sum_between = sum(arr[first_pos + 1:second_pos])
        print(f"Сумма элементов между {first_pos + 1}-м и {second_pos + 1}-м положительными элементами: {sum_between}")
    else:
        print("Между первым и вторым положительными элементами нет других элементов — сумма = 0.")

# Перемещаем нули в конец массива
non_zeros = [x for x in arr if x != 0]
zeros = [x for x in arr if x == 0]
arr_transformed = non_zeros + zeros

print("Преобразованный массив (нули в конце):", arr_transformed)

