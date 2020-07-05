import csv
filename = input("Enter file name : ")
my_tuple = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
with open(filename+".csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "address", "age"])
    writer.writerows(my_tuple)
