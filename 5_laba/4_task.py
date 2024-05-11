def reverse_dict(original_dict):
    reversed_dict = {}
    for key, value in original_dict.items():
        reversed_dict[value] = key
    return reversed_dict

# Пример использования
original_dict = {1: 'apple', 2: 'banana', 3: 'orange'}
reversed_dict = reverse_dict(original_dict)
print(reversed_dict)  # Выведет: {'apple': 1, 'banana': 2, 'orange': 3}
