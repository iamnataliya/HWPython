# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
n = int(input('input number: '))
sum = 0
while n >0:
    digit = n % 10
    sum += digit
    n //=10
print ("Sum of numbers:", sum)
# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input('input number: '))
def get_numbers(N):
    return [i for i in range(1, N + 1)] 
print(get_numbers(N))

def get_factorial(N):
    if(N==1 or N==0):
        return 1
    else:
        return N*get_factorial(N-1)

print("The factorial of ",N," is: ",get_factorial(N))

# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму
n = int(input('input number: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))
# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# Я первый раз так решила)
# import random
# psw = '' 
# for x in range(12):
#     psw = psw + random.choice(list('123456789qwertyuiopasdfgh'))
# print(psw)

import time

def my_randome(min=0, max=10):
    result=min-1
    digit = len(str(max))
    while result < min or result > max:
        string_time = str(time.time_ns()//100)
        result = int(string_time[digit: len(string_time)])
        return result
min_value = 1
max_value = 50
for i in range(0,20):
    start = time.time_ns()
    print(my_randome(min_value,max_value), end = ' ')
    finish = time.time_ns()
print('\n', finish-start)
