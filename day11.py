# Day 11: Function & return 

def information(numbers):
    total = 0 
    for num in numbers:
        total = total + num 
    return total 

marks = [ 35, 65, 85 ]
result = information(marks)
print(result)
 
