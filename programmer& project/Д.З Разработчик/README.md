# Урок 1. Знакомство с Python
задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

*Пример:*

- 6 -> да
- 7 -> да
- 1 -> нет
- 
задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

*Пример:*

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3

# Урок 2. Знакомство с Python. Продолжение
Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

*Пример:*

- 6782 -> 23
- 0,56 -> 11

Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой. COUNT или FIND или SPLIT нельзя юзать! говорил же на семинаре.

# Урок 3. Данные, функции и модули в Python
Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.

*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10

# Урок 4. Данные, функции и модули в Python. Продолжение
задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
можно юзать библиотекe re

задача 1. Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

Делаем игру против бота

а) Подумайте как наделить бота ""интеллектом""

задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ EVAL! максимум для тестирования

Задача 1. Создайте программу для игры в "Крестики-нолики".

Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

*Пример:* 

2+2 => 4; 

1+2*3 => 7; 

1-2*3 => -5;

- Добавьте возможность использования скобок, меняющих приоритет операций.

    *Пример:* 

    1+2*3 => 7; 

    (1+2)*3 => 9;
    
# Урок 7. Python: от простого к практике
Задание в группах: Добить калькулятор. Создать репо в гитхабе , скинуть туда всё и обязательно скрины работы всех модулей! в Readme описать архитектуру приложения, указать кто над каким модулем работал.

на ОТЛИЧНО - должно быть логгирование, функции eval не должно быть, грамотный и красивый ридми, где приложено описание работы приложения + модульная архитектура. Тем , кто делает в одиночку, можно юзать eval
для комплексных чисел. Если команда разработала графический интерфейс, то комплексные числа может не делать.

На ХОРОШО - допускается eval для комплексных чисел.

На УДОВЛ - можно везде юзать eval.

# Урок 8. Python: от простого к практике. Продолжение
Доделать решение задачи: Задача: Создать информационную систему для работы с какой либо предметной областью.

ОБязательные требования:

1. разбиение на модули.

2. внешнее хранилище информации (или БД или файл формата txt / json / csv)

3. Функционал по просмотру, поиску, добавлению, редактированию, удалению информации.

Плюсами будет наличие ГУИ и/или наличие настоящей БД (SQLite3 / PostgreSQL)
 
 
# Урок 9. Возможна ли жизнь без PIP?
Напоминаю про грамотное оформление readme.md в ваших проектах. За отсутствие оформления буду снижать оценку.

Прикрутить телеграм - бота к задачам с предыдущего семинара:

1. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования. Желательно соблюсти разбиение на модули.

2.Игра в крестики-нолики.

Одну из задач вы можете на выбор заменить созданием своего тг-бота с определенным функционалом и использованием API. То есть чтобы бот дергал информацию откуда-то, как сделано в буткемпе.

