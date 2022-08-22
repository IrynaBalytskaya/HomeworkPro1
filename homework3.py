# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))
# d = int(input('d='))
#
# if a > b and a > c and a > d:
#     print('Наибольшее число: a')
# elif b > c and b > d:
#     print('Наибольшее число: b')
# elif c > d:
#     print('Наибольшее число: c')
# else:
#     print('Наибольшее число: d')
#
#
# flat = int(input( 'Номер квартиры: '))
# if flat >= 1 and flat <= 144:
#     entrance = (flat - 1) // 36 + 1
#     floor = (flat - 1) % 36 // 4 + 1
#     print(entrance, floor)
# else:
#     print('Нет такой квартиры')
#
#
# year = int(input('Enter year= '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(366)
# else:
#     print(365)

a = int(input('Сторона a= '))
b = int(input('Сторона b= '))
c = int(input('Сторона c= '))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print('Треугольник существует')
else:
    print('Треугольник не существует')

