class SumZero:
    def __init__(self,list1):
        self.list1=list1

    def getList(self):
        n=len(self.list1)
        flag = True
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (self.list1[i] + self.list1[j] + self.list1[k] == 0):
                        print(self.list1[i], self.list1[j], self.list1[k])
                        flag = True
        if (flag == False):
            print(" not exist ")

list2 = [-25, -10, -7, -3, 2, 4, 8, 10]
s1=SumZero(list2)
s1.getList()