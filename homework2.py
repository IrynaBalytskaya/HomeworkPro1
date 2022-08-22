import math

str = '123'
print(int(str))

int = 123
print(float(int))

float = 12.345
print(int(float))

a = int(input('Введите номер карты: '))
print(a % 10000)

num = int(input("Введите целое: "))
a = num // 100
b = num % 100
c = b // 10
d = b % 10
print(a + c + d)

a = int(input('Сторона а= '))
b = int(input('Сторона b= '))
c = int(input('Сторона c= '))

p = (a + b + c)/ 2

square = math.sqrt(p *(p - a)*(p - b)*(p - c))
print(square)

a = int(input('Введите число: '))
print(a >= 20)

a = int(input('Введите число: '))
print(a == 0)

a = int(input('Введите число: '))
print(bool(a % 2))

a = int(input('Число 1: ' ))
b = int(input('Число 2: ' ))
c = int(input('Число 3: ' ))
print(max(a, b, c))








