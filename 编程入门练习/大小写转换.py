v = (ord('a') - ord('A'))
def toLowerCase(string:str):
    result = ""

    for i in range(len(string)):
        var1 = string[i]
        ascii = ord(var1)
        if var1 >= 'A' and var1 <= 'Z':
            var1 = chr(ascii + v)
        #if ascii >= 65 and ascii <= 90:
            #var1 = chr(ascii + 32))
        result += var1

    return result

def toUpperCase(string:str):
    result = ""
    for var1 in string:
        ascii = ord(var1)
        if var1 >= 'a' and var1 <= 'z':
            var1 = chr(ascii - v)
        #if ascii >= 65 and ascii <= 90:
            #var1 = chr(ascii - 32))
        result += var1

    return result

string = "abcDEFgh"
lower = toLowerCase(string)
print(lower)
upper = toUpperCase(string)
print(upper)

