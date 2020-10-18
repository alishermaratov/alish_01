"""сортировка  вставками """
def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i
        while (j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        array[j] = key

print("Сортировка вставками")
arr = []
length = int(input("Введите длину массива: "))
for i in range(0, length):
    element = int(input("arr[" + str(i + 1) + "] = "))
    arr.append(element)
insertion_sort(arr)
print("Отсортированный массив: ")
print(arr)





def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)



def insertion_sort(nums):
    # Начнем со второго элемента, так как мы предполагаем, что первый элемент отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # И сохранить ссылку на индекс предыдущего элемента
        j = i - 1
        # Переместить все элементы отсортированного сегмента вперед, если они больше, чем элемент для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert
# Проверяем, что это работает
random_list_of_nums = [9, 1, 15, 28, 6]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)
