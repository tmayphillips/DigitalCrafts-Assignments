numbers = [2,1,45,67,89,4,5,7,9]
ascend_numbers = []
descend_numbers = []

def ascend(numbers): 
    n = len(numbers) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if numbers[j] > numbers[j+1]: 
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    for i in range(len(numbers)): 
        ascend_numbers.append("%d" %numbers[i])

def descend(numbers): 
    n = len(numbers) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if numbers[j] < numbers[j+1]: 
                numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
    for i in range(len(numbers)): 
        descend_numbers.append("%d" %numbers[i])

ascend(numbers)
descend(numbers)
print(ascend_numbers)
print(descend_numbers)
