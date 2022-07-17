# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

numbers = list(range(1, 10))
print(numbers)
print(sum(numbers[1::2]))

# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
numbers = list(range(1, 7))
result = []
print(numbers)
for i in range((len(numbers)+1)//2):
     result.append(numbers[i]*numbers[len(numbers)-1-i])
print(result)

# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

numbers = [1.7,1.9,2.9,9.08,10,-3.09]
print(numbers)
result = []
min = 1
max = 0
for i in numbers:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(max-min)