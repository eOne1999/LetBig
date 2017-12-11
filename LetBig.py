# -*- coding: utf-8 -*-

from data import symbols, strings

f = open('text.txt', 'w')  # открываем (создаём) файл для вывода

text = input('Enter the text (you can use only a-z (A-Z), а-я (А-Я), 0-9 and any symbols on your keyboard):\n')
text = text.lower()  # одинаковый регистр

for i in range(strings):     # идём по строкам
    for char in text:           # идём по символам в введённом тексте
        if char in symbols:           # проверка на наличие символа в словаре
            for element in symbols[char][i]:      # идём по словарю
                if element != '':
                    f.write(char.upper())                 # делаем символ большим и выводим его в файл
                else:
                    f.write(' ')                          # пробел между СИМВОЛАМИ
            f.write(' ')
    f.write('\n')               # переходим на новую строку в strings

print('\nLook the result in text.txt :)')
