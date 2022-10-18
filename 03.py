# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

from unittest import result


limit = int(input('Введите границу диапозона: '))
numbs = []
for i in range(-limit,limit + 1):
    numbs.append(i)
print(numbs)

index = []
for i in input('Введите индексы: ').split():
    index.append(int(i))

result = 1
for idx in index:
    result *= numbs[idx]
print(f'Произведение равно {result}') 