def getInput():
    return input("Введите данные: ")

def testInput(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def strToInt(value):
    return int(value)

def printInt(value):
    print(value)

input_value = getInput()
is_int = testInput(input_value)

if is_int:
    int_value = strToInt(input_value)
    printInt(int_value)
