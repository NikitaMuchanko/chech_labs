def transform_string(s):
    
    lower_count = sum(c.islower() for c in s)
    upper_count = sum(c.isupper() for c in s)
    
    if lower_count >= upper_count:
        return s.lower()
    elif upper_count > lower_count:
        return s.upper()
    else:
        return s  


input_string = "HeLLo World"
output_string = transform_string(input_string)
print(output_string)  
