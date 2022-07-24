# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1
import math
d = float(input('Set the accuracy d = 0.____: '))

def pi(): #1 варинат решения
    p = 3
    for i in range(2, 50, 4):
        p+= 4/(i*(i+1)*(i+2) - 4/((i+2)*(i+3)*(i+4)))
    return p

cnt = pi()//d*d
print(cnt)

def gauss_Pi(d): #2 варинат решения
    accuracy = 1
    pi_Gauss = 48*math.atan(1/18)+32*math.atan(1/57)-20*math.atan(1/239)
    number_of_digit = int(len(str(d).split(".")[1]))
    while number_of_digit > 0:
        accuracy*=10
        number_of_digit-=1
    return int(pi_Gauss*accuracy)/accuracy
print(gauss_Pi(d))

# 2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = input("Enter the sequence (separated by commas): \r\n").replace(' ','').split(',')

result_list = []

for i in my_list:
    flag = False
    for j in result_list:
        if j == i:
            flag = True
            break
    if flag:
        continue
    else:
        result_list.append(i)

print(result_list)

# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

number = int(input("Input number: "))

result = []
while(number != 1):
    for i in range(2, number + 1):
        if(number % i == 0):
            result.append(i)
            number //= i
            break

print(set(result))

# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.
file = open('Text.txt', "w", encoding='utf-8')
file.write("Мама сшила м0не штаны и7з бере9зовой кор45ы 893.")
file.close()

path = 'Text.txt'

def delete_nums(path: str) -> str:

    file = open('Text.txt' , "r",encoding='utf-8')
    data = file.read()
    list_of_words = data.split()
    file.close()

    new_list = []
    for i in list_of_words:
        delete_bool = False
        for n in i:
            if n.isdigit():
                delete_bool = True
                break
        if delete_bool == False:
            new_list.append(i)

    return  f"{list_of_words} -> " + " ".join(new_list) 
    
print(delete_nums(path))