# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce

# 1- Определить, присутствует ли в заданном списке строк, некоторое число
def find_number(list_of_text: str, number: str):
    return len(list(filter(lambda a: a in number, list_of_text.split()))) > 0


text = "jhvfd dhf bla 22 sdh"
number = "22"
print(f"{number} in text : '{text}' - > is {find_number(text, number)}")
# 2- Найти сумму чисел списка стоящих на нечетной позиции
def sum_odd_index(list_of_num : list):
    sum_of_num = 0
    for i in list(filter(lambda a : list_of_num.index(a)%2 != 0  , list_of_num)):
        sum_of_num += i
    return sum_of_num

list_of_num = [1,2,3,4,5,6,7,8,9]
print(f"sum of nums with odd index in {list_of_num} => {sum_odd_index(list_of_num)} ")
# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
list_of_coord = "1 2 5 6"

def distance_between_two_dots(text : str):
    x1,y1,x2,y2 = list(map(int ,text.split()))
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

print(f"distance between x1,y1,x2,y2 [{list_of_coord}] -> {distance_between_two_dots(list_of_coord):.2f}")
# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
def look_up_second_pos(list_where,str_what):
    count = 0
    for i,item in enumerate(list_where):
        if item == str_what:
            count +=1
            if count ==2:
                break
    if count>0:
        return i
    else:
        return -1

    
text = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
to_find = "qwe"

print(f"список: {text}, ищем: '{to_find}', ответ: {look_up_second_pos(text,to_find)}")
# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def multi_pairs(list_num):
    new_list = []
    for i in range((int(len(list_num)//2)+int(len(list_num)%2))):
        new_list.append(list_num[i]*list_num[-1-i])
    return new_list

list_num = [1,2,3,4,5,6]

print(f"{list_num} - > {multi_pairs(list_num)}")
# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
def list_N(number_N):
    list_of_num = [1]
    for i in range(1,number_N):
        list_of_num.append(list_of_num[i-1]*-3)
    return list_of_num

number_N=5
print(f"For N = {number_N} -> {list_N(number_N)}")