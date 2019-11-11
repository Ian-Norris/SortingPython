#Merge sort help
#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
import random


def swap_in_list(data, elem1, elem2):
    holder = data[elem1]
    data[elem1] = data[elem2]
    data[elem2] = holder
    return data


def bubble_sort(data):

    length_data = len(data)
    for j in range(length_data):
        for i in range(length_data-1):
            if data[i] > data[i+1]:
                swap_in_list(data, i, i+1)
    return data


def find_lowest(data):
    cur_lowest = (data[0], 0)
    for i in range(len(data)):
        if data[i] < cur_lowest[0]:
            cur_lowest = (data[i], i)
    return cur_lowest


def selection_sort(data):
    length_data = len(data)
    cur_lowest = data[0]
    for i in range(length_data):
        cur_lowest = find_lowest(data[i:length_data])
        if data[i] > cur_lowest[0]:
            holder = data[i]
            data[i] = cur_lowest[0]

            #Adding i here for an offset, which is the current location of the pointer
            data[cur_lowest[1]+i] = holder
    return data


def insertion_sort(data):
    length_data = len(data)

    pos = 0
    for i in range(length_data):
        sorted = False
        if pos != 0:
            pos = i - 1
        while not sorted:
            if pos < 0:
                sorted = True
                pos -= 1
                break
            elif data[i] >= data[pos]:
                sorted = True
                pos -= 1
                break
            else:
                holder = data[i]
                data[i] = data[pos]
                data[pos] = holder
                i -= 1
            pos -= 1


def merge_sort(data):

    if len(data) // 2 > 0:
        length_data = len(data)
        middle = (length_data // 2)

        left = data[:middle]
        right = data[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


def quick_sort(data):
    lesser = []
    greater = []
    equal = []
    if len(data) > 1:
        # pivot is finding a middle element
        pivot = data[len(data)//2]
        for x in range(len(data)):
            if data[x] == pivot:
                equal.append(data[x])
            elif data[x] > pivot:
                greater.append(data[x])
            elif data[x] < pivot:
                lesser.append(data[x])
        return quick_sort(lesser) + equal + quick_sort(greater)
    else:
        return data


def random_list():
    list1 = []
    for i in range(random.randint(1,50)):
        list1.append(random.randint(1,50))
    return list1


def main():
    # Bubble sort
    list1 = random_list()
    print('List before bubble sorting:\n', list1, sep='')
    bubble_sort(list1)
    print('List after bubble sorting\n', list1, sep='')
    print()

    # Selection Sort
    list2 = random_list()
    print('List before selection sorting:\n', list2, sep='')
    selection_sort(list2)
    print('List after selection sorting\n', list2, sep='')
    print()

    # Insertion Sort
    list3 = random_list()
    print('List before insertion sorting:\n', list3, sep='')
    insertion_sort(list3)
    print('List after insertion sorting\n', list3, sep='')
    print()

    # Merge Sort
    list4 = random_list()
    print('List before merge sorting:\n', list4, sep='')
    merge_sort(list4)
    print('List after merge sorting\n', list4, sep='')
    print()

    # Quick Sort
    list5 = random_list()
    print('List before quick sorting:\n', list5, sep='')
    list5 = quick_sort(list5)
    print('List after selection sorting\n', list5, sep='')
    print()

    input("Hit enter to close... ")

main()


