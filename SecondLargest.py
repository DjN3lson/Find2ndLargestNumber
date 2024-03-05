def second_largest(numbers):
    mx = max(numbers[0], numbers[1]) 
    secondmax = min(numbers[0], numbers[1]) 
    n = len(numbers)
    
    for i in range(2,n): 
        if numbers[i] > mx: 
            secondmax = mx
            mx = numbers[i] 
        elif numbers[i] > secondmax and mx != numbers[i]: 
            secondmax = numbers[i]
        elif mx == secondmax and secondmax != numbers[i]:
            secondmax = numbers[i]
    return secondmax

numbers = [5, 5, 2, 2, 1, 1, 4, 4]
result = second_largest(numbers)
print(result)
