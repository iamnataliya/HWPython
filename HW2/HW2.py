# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# n = int(input('input number: '))
# sum = 0
# while n >0:
#     digit = n % 10
#     sum += digit
#     n //=10
# print ("Sum of numbers:", sum)
# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input('input number: '))
def get_numbers(N):
    return [i for i in range(1, N + 1)] 
print(get_numbers(N))
# //дальше надо придумать как считать