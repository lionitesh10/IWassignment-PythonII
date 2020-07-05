def createlist():
    friend = []
    n = int(input("Enter no of friends to add in list : "))
    for i in range(n):
        friend.append(input())
    return friend


def search(list1, value):
    for i in list1:
        if i == "John":
            print("Found")
            break
    else:
        print("not found")

l1 = createlist()
search(l1, "John")
