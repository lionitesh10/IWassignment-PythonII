def createList():
    people = []
    n = int(input("Enter no of people to add "))
    for i in range(n):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = input("Enter your age: ")
        if age == "":
            age = None
        friend_tuple = first_name, last_name, age,
        people.append(friend_tuple)
    return people


def avgAge(list1):
    avg = 0
    l = 0
    for i in list1:
        if i[2] == None:
            continue
        else:
            avg += int(i[2])
            l += 1
    avg = avg/l
    for i in list1:
        if i[2] == None:
            continue
        elif int(i[2]) > avg:
            print("Old : ", i)
        elif int(i[2]) == avg:
            print("Average : ", i)
        else:
            print("Young : ", i)


l1 = createList()
avgAge(l1)
