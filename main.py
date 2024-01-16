numbers = list(map(int, input("Введите числа через пробел: ").split()))

non_zero_index = 0

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[non_zero_index], numbers[i] = numbers[i], numbers[non_zero_index]
        non_zero_index += 1

print(f"Результат: {' '.join(map(str, numbers))}")
