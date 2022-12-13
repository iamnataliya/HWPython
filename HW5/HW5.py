# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"
line = 'Абвгдейка - это передача'.lower()

words = line.split(' ')

fragment = 'абв'
new_words = []
for word in words:
     if fragment not in word:
         new_words.append(word)

line = ' '.join(new_words)
print (line)

# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
def FirstFunc(langs, nums):
    for i in range(len(langs)):
        langs[i] = langs[i].upper()
    return list(zip(nums, langs))
def SecFunc(inpt_list: list):
    result_list = []
    for i in inpt_list:
        summ = 0
        word = i[1]
        for letter in word:
            hex_code = ord(letter)
            summ += int(hex_code)
        if summ % i[0] == 0:
            result_list.append((summ, i[1]))
    return result_list

languages = ["python", "c#", "java", "pascal", "php"]
numbers = [i for i in range(1, len(languages) + 1)]

my_first_list = FirstFunc(languages, numbers)

print(f"Вывод первой функции:\r\n{my_first_list}")

print(SecFunc(my_first_list))

# def filter_by_points(tuples_list):
#     result_list = []
#     result = 0
#     for number, language in tuples_list:#range(len(), 0, -1)
#         points = reduce(lambda a,b: a+b, [ord(char) for char in language])
#         if points % number == 0:
#             result += points
#             result_list.append((points, language))
#     del tuples_list
#     return result, result_list
#     with open('candy-game\program_langs.txt', encoding='utf-8') as file:
#         languages = file.read().split('\n')
#     numbers = list(range(1, len(languages)+1))
#     #tuples_list = enumerate([word.upper() for word in languages])
#     tuples_list = zip(numbers, [word.upper() for word in languages])
#     return list(tuples_list)

# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах
