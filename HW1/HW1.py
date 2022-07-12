# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
num_day = int(input('input the day '))
if 1 < num_day > 7:
    print('mistake')
elif num_day == 5:
    print('Thaks God it is Friday!')
elif num_day == 6 or num_day == 7:
    print('weekend!')
else:
    print('working day')
# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print ('\nX \t Y \t Z \t ¬(X ⋁ Y ⋁ Z) \t ¬X ⋀ ¬Y ⋀ ¬Z \t ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \n')
x = True
y = False
z = True

left = not(x or y or z)
right = not(x) and not(y) and not(z)

print(left == right)
# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
num_x = int(input('enter the coordinates Х '))
num_y = int(input('enter the coordinates Y '))
if num_x == 0 or num_y == 0:
    print('mistake')
elif num_x > 0 and num_y > 0:
    print('1')
elif num_x < 0 and num_y > 0:
    print('2')
elif num_x < 0 and num_y < 0:
    print('3')
else:
    print('4') 
# 4- Напишите программу, которая по заданному номеру четверти, показывает деапозон возможных координат точек в этой четверти (x и y).
quater_number = int(input('input quater '))
if 4 < quater_number > 0:
    print('mistake')
elif quater_number == 1:
    print(' range x > 0 и y > 0')
elif quater_number == 2:
    print(' range x < 0  и y > 0')
elif quater_number == 3:
    print(' range x < 0 и y < 0')
else:
    print(' range x > 0 и y < 0')
# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from math import sqrt

num_x1 = int(input('enter the coordinates Х1 '))
num_y1 = int(input('enter the coordinates Y1 '))
num_x2 = int(input('enter the coordinates Х2 '))
num_y2 = int(input('enter the coordinates Y2 '))
result = sqrt((num_x2 - num_x1) ** 2 + (num_y2 - num_y1)**2)
print('%.2f' % result)
