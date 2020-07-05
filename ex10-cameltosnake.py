def camelToSnake(my_string, separator):
    result = [my_string[0].lower()]
    for ch in my_string[1:]:
        if ch in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            result.append(separator)
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)


ccase = input("Enter camel case : ")
separator = input("Enter separator character : ")
print(camelToSnake(ccase, separator))
