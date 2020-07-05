def calc(a,b,op):
    a=exception(a)
    b=exception(b)
    if a=="False":
        print("Unable to Convert String to Int for a ..")
    elif b=="False":
        print("Unable to Convert String to Int for b ..")
    else:
        if op=="+":
            print(a+b)
        elif op=="-":
            print(a-b)
        elif op=="*":
            print(a*b)
        elif op=="/":
            try:
                div= a/b
                print(div)
            except ZeroDivisionError:
                print("Not divisible by zero .. Sorry")

def exception(a):
    try:
        i=int(a)
        return i
    except ValueError:
        return "False"

calc("a",10,"+")
calc(10,"b","-")
calc(10,20,"+")
calc(10,0,"/")