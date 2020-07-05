def createList():
    my_name = "Nitesh", "Sapkota", 21,
    people = []
    people.append(my_name)
    n = int(input("Enter no of people to add "))
    for i in range(n):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter your age: "))
        friend_tuple = first_name, last_name, age,
        people.append(friend_tuple)
    return people


l1 = createList()


def sorttuplelist(people):
    people.sort(key=lambda x: x[2])
    return people


print(sorttuplelist(sorttuplelist(l1)))
