def binary_search(list1, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if list1[mid] == x:
            return mid
        elif list1[mid] > x:
            return binary_search(list1, low, mid - 1, x)
        else:
            return binary_search(list1, mid + 1, high, x)
    else:
        return -1


def createAndSort():
    n = int(input("Enter no of elements in list"))
    l1 = []
    print("Enter array Elements : ")
    for i in range(n):
        l1.append(int(input()))
    l1 = sorted(l1)
    x = int(input("Enter element to search "))
    result = binary_search(l1, 0, len(l1)-1, x)
    return (result, x)


result, x = createAndSort()
if result == -1:
    print("Element not found ")
else:
    print("{0} present at index {1}".format(x, result))
