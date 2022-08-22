# Напишите программу, которая переведет целое число (от 1 до 100) из
# римской записи в обычные цифры.
# Например: XXII -> 22
# number = input("Введите число от 1 до 100: ")
# a = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VI': 7, 'VI': 8, 'IX': 9, 'X': 9}
# b = {'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90}
# c = {'C': 100}
# for i in a:
#     if number.find(i.key):
#         print(i.value)
#         break
#print(a.get(number))
from string import punctuation
text_1 = input('Write text: ')
text_2 = input('Write text2: ')

for item in punctuation:
    text_1 = text_1.replace()
    text_2 = text_2.replace()
text_1 = text_1.split()
text_2 = text_2.split()


x = text_1 | text_2
print(x)




