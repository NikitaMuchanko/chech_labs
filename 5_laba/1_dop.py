dictionary = {1: 'acc', 2: 'cab', 3: 'ccb'}
def reverse(dictionary):
    temp_dict = {}
    for i in dictionary.items():
        for i1 in i[1]:
            if i1 not in temp_dict:
                temp_dict[i1] = str(i[0])
            else:
                temp_dict[i1] += str(i[0])
    return temp_dict
print(reverse(dictionary))
