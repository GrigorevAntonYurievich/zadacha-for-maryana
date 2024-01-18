numbers = input("Введите список чисел через пробел: ").split()

numbers = list(map(int, numbers))

max_count = 0  
most_common_number = None  

for num in numbers:
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        most_common_number = num

print("Число: ", most_common_number)
