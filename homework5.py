import math
#Напишите программу, которая посчитает сколько букв «b» в введенной строке текста.
str = input("Enter text: ")
str_b = str.count('b')
print(str_b)

#Считайте строку, которая будет представлять имя человека, введенное с клавиатуры.
#Проверьте эту строку на валидность.
#Имеется в виду, что например, в имени человека не может быть цифр,
#оно должно начинаться с большой буквы, за которой должны следовать маленькие.
str = input('Введите ваше имя: ')
res = 

# Выведите на экран 5 строк со значением числа Pi.
# В первой строке должно быть 2 знака после запятой, во второй 3 и так далее.
text_1= 'Pi = {:.2f}'.format(math.pi)
text_2 = 'Pi = {:.3f}'.format(math.pi)
text_3 = 'Pi = {:.4f}'.format(math.pi)
text_4 = 'Pi = {:.5f}'.format(math.pi)
text_5= 'Pi = {:.6f}'.format(math.pi)
print(text_1)
print(text_2)
print(text_3)
print(text_4)
print(text_5)

# Дано четырехзначное число. Проверить, является ли оно «счастливым билетом».
# Примечание: счастливым билетом называется число, в котором, при четном количестве цифр в числе,
# сумма цифр его левой половины равна сумме цифр его правой половины. Например, рассмотрим число 1322.
# Его левая половина равна 13, а правая 22, и оно является счастливым билетом (т. к. 1 + 3 = 2 + 2).
str = input('Введите четырехзначное число: ')
if not str.isdigit() or not len(str) == 4:
     print('некорректное число')
else:
    left = int(str[0]) + int(str[1])
    right = int(str[2]) + int(str[3])
    if left == right:
         print("Билет счастливый")
    else:
         print("не повезло тебе чувак")


# С клавиатуры вводится шестизначное число.
# Проверить, является ли оно палиндромом.
# Примечание: палиндромом называется число, слово или текст,
# которые одинакового читаются слева направо и справа налево.
# Например, это числа 143341, 5555, 7117 и т. д.
sss = input("num= ")
sss_two = sss[::-1]
if sss == sss_two:
    print("works!")
else:
    print("not works")


# Есть круг с центром в начале координат и радиусом 4.
# Пользователь вводит с клавиатуры координаты точки x и y.
# Написать программу, которая определит, лежит ли эта точка внутри круга или нет.
 x = int(input('x ='))
 y = int(input('y ='))
 r = int(input('r ='))
 if x ** 2 + y ** 2 < r ** 2:
     print("Точка внутри")
 else:
     print("Точка не внутри")

#Вводится строка из слов, разделенных пробелами.
# Найти самое длинное слово и вывести его на экран.
str = input('Enter text: ').split()
print(max(str), key=len)






