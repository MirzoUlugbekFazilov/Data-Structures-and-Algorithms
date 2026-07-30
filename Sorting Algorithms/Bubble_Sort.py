
numbers = [1, 5, 2, 20, 3] 

print(numbers)

sorted = False

while not sorted:
    sorted = True
    for i in range(len(numbers)-1):
        second = numbers[i+1]
        if numbers[i]>numbers[i+1]:
            numbers[i+1] = numbers[i]
            numbers[i] = second
            sorted = False
        else:
            pass


print(numbers)


    

