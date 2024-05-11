def check_conditions(x):
  
    is_three_digit_with_zero = 100 <= x < 1000 and x % 10 == 0
    
    
    is_odd_and_divisible_by_3_or_5 = x % 2!= 0 and (x % 3 == 0 or x % 5 == 0)
    
    
    is_in_range = 2 <= x <= 6
    
   
    is_all_digits_same = x // 10 == x % 10
    
    result = is_three_digit_with_zero and is_odd_and_divisible_by_3_or_5 and is_in_range and is_all_digits_same
    
    return result


x = int(input("Введите число "))
print(check_conditions(x))  
