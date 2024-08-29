import random

def getList(min, max):
    return list(range(min, max+1))

def swap(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

def moveBack(lst, pos):
    while pos > 0 and lst[pos] < lst[pos-1]:
        swap(lst, pos, pos-1)
        pos-=1
    return lst

def insertionSort(lst):
    for i in range(1, len(lst)):
        lst = moveBack(lst, i)
    return lst

def is_sorted(lst):
    return all(lstc[i] <= lst[i + 1] for i in range(len(lst) - 1))

#creating and shuffling an array
nums = getList(1,100)
random.shuffle(nums)

print(nums)
print(insertionSort(nums))