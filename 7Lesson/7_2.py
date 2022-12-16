list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def binary_search(list, element):
    list.sort()
    start = 0
    end = len(list)
    while start <= end:
        centr = (start + end) // 2
        if element == centr:
            return list.index(element), centr
        else:
            if element > centr:
                start = centr +1
            else:
                end = centr -1
    return "no element"

print(binary_search(list, 11))
