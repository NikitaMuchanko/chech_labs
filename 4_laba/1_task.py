def getInput():
    return input("Введите два значения через пробел ").split()

def testInput(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def strToInt(value):
    return int(value)

def printInt(value):
    print(value)


values = getInput()
is_number = testInput(values[0]) and testInput(values[1])

if is_number:
    int_value1 = strToInt(values[0])
    int_value2 = strToInt(values[1])
    printInt(int_value1 + int_value2)
else:
    printInt(values[0] + values[1])
