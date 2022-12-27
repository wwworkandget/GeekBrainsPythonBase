# Задача 1.
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('task_5_1_file.txt', "w", encoding='utf-8') as file:
    START = True
    while START:
        line = input()
        file.write(line + '\n')
        if not line:
            START = False
