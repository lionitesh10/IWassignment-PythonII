def friendslist():
    friend = []
    print(id(friend))
    n = int(input("Enter no of friends to add in list : "))
    for i in range(n):
        friend.append(input())
    print(id(friend))
    slist = sorted(friend)
    print("1st item on the list : {0} and 2nd item on the list : {1}".format(
        slist[0], slist[1]))


friendslist()
