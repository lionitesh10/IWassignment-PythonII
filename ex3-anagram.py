paragraph = """ car rac cab abc my name"""


def stringToList(paragraph):
    return paragraph.split()


def anagramsList(l):
    alist = []
    for i in range(len(l)):
        for j in range(len(l)):
            if (l[i] != l[j]) and (sorted(l[i]) == sorted(l[j])):
                alist.append(l[i])
                alist.append(l[j])

    return list(set(alist))


list1 = stringToList(paragraph)
print(anagramsList(list1))
