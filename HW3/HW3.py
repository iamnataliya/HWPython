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
# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def num_biger_then_zero(text):

    int_num = True
    while int_num:
        n = input(f"{text}")
        if n.isdigit():
            n = int(n)
            if n <= 0:
                print("Input number > 0")
            else:
                int_num = False
        else :
            print("Wrong number")
    return n
n = num_biger_then_zero("Input number: ") 
ost = ''  
while n > 0:  
    ost = str(n % 2) + ost 
    n = n // 2 

print(f'Binary number: {ost}')
# Простой вариант 
  a = int(input('Input numbers ='))
  b = ''
    while a > 0:
        b = str(a % 2) + b
        a = a // 2
    print('Binary number: ', b)


# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Фибоначи для положительных чисел
def fib(n):
    if n in [1, 2]:
      return 1
    else:
      return fib(n-1) + fib(n-2)
    list = []
    for e in range(1, 10):
    list.append(fib(e))
    print(list) # 1 1 2 3 5 8 13 21 34

# Решение корректное 
def fib(n):
    if (n <= 1):
        return n
    else:
        return (fib(n-1) + fib(n-2))
n = int(input("input number to make the fibonacci sequence:"))
positive_lst=[]
for i in range(n):
    positive_lst.append(fib(i))
print(f'Positive: \n{positive_lst}')
negative_lst =[]
my_lst = positive_lst
for i in range(1, len(my_lst)):
    negative_lst.append(my_lst[i]*((-1)**(i+1)))

negative_lst.reverse()

print(f'Negative: \n{negative_lst + my_lst}')
# F−n = (−1)^(n+1)*F(n).

