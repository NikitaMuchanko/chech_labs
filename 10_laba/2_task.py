from math import *
from timeit import *
import time

# Открытие файла и чтение первых 100 строк
file = open("pi-10million.txt", "r")
first_hundred_lines = file.readlines(100)

# Создание списка чисел от 1 до 10 миллионов
sorted_numbers = sorted([int(i) for i in range(1, 10000000)])

def binary_search(numbers_list, target_number):
    start_index = 0
    end_index = len(numbers_list)
    
    while start_index < end_index:
        middle_index = (start_index + end_index) // 2
        if target_number == numbers_list[middle_index]:
            return middle_index
        elif target_number < numbers_list[middle_index]:
            end_index = middle_index
        else:
            start_index = middle_index + 1

def golden_ratio_search(target_value, array):
    golden_ratio = 0.5 * (1 + 5**0.5)
    lower_bound = 0
    upper_bound = len(array) - 1
    
    while upper_bound - lower_bound > 1:
        split_point_1 = int(upper_bound - ((upper_bound - lower_bound) / golden_ratio))
        split_point_2 = int(lower_bound + ((upper_bound - lower_bound) / golden_ratio))
        
        subset_A = array[lower_bound : split_point_2 + 1]
        subset_B = array[split_point_1 : upper_bound + 1]
        
        if target_value in subset_A:
            upper_bound = split_point_2
        elif target_value in subset_B:
            lower_bound = split_point_1
        else:
            print('goldenRatioSearch: not found')
            return
        
    return lower_bound

def interpolating_search_algorithm(sorted_array, value_to_find):
    lower_limit = 0
    upper_limit = len(sorted_array) - 1
    
    while lower_limit <= upper_limit:
        index = lower_limit + ((upper_limit - lower_limit) * (value_to_find - sorted_array[lower_limit]) // (sorted_array[upper_limit] - sorted_array[lower_limit]))
        
        if value_to_find == sorted_array[index]:
            return index
        elif value_to_find < sorted_array[index]:
            upper_limit = index - 1
        else:
            lower_limit = index + 1

# Время выполнения бинарного поиска
binary_search_time = default_timer()
print(binary_search(sorted_numbers, 9999999))
print('{:.10f}'.format(default_timer() - binary_search_time))

# Время выполнения поиска с использованием золотого деления
golden_ratio_search_time = default_timer()
print(golden_ratio_search(9999999, sorted_numbers))
print('{:.10f}'.format(default_timer() - golden_ratio_search_time))

# Время выполнения интерполяционного поиска
interpolating_search_time = default_timer()
print(interpolating_search_algorithm(sorted_numbers, 9999999))
print('{:.10f}'.format(default_timer() - interpolating_search_time))
