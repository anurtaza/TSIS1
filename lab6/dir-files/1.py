import os
from string import ascii_uppercase

#task1
path = open('/Users/ayaulymnurtaza/Downloads/lab6/text.txt')

print("Список директорий")

for entry in os.scandir(path):
    if entry.is_dir():
        print(entry.name)

print("\nСписок файлов")

for entry in os.scandir(path):
    if entry.is_file():
        print(entry.name)

print("\nОбщий список")

for entry in os.scandir(path):
    print(entry.name)

 #task2
if os.path.exists(path):
    print("Путь существует")
else:
    print("Путь не существует")

if os.access(path, os.R_OK):
    print("Можно читать путь")
else:
    print("Невозможно читать путь")

if os.access(path, os.W_OK):
    print("Можно записывать в путь")
else:
    print("Невозможно записывать в путь")

if os.access(path, os.X_OK):
    print("Можно выполнять путь")
else:
    print("Невозможно выполнять путь")


#task3
if os.path.exists(path):
    head, tail = os.path.split(path)
    print(f"Имя файла: {tail}")
    print(f"Часть каталога: {head}")
else:
    print("Указанный путь не существует.")

#task4

with open(path, 'r') as file:
    line_count = sum(1 for line in file)

print(f'Количество строк в файле: {line_count}') 

#task5

mylist = ['A', 'B', 'C', 'D']

with open('/Users/ayaulymnurtaza/Downloads/lab6/dir-files/demofile.txt' , 'w') as file:
    for i in mylist:
        file.write(i + '\n')
file.close()

#task6

for char in ascii_uppercase:
    file = open('/Users/ayaulymnurtaza/Downloads/lab6/{fchar}'.format(fchar = char), 'x')
    file.close()

#task7 скопировать содержимое файла в другой файл

with open('/Users/ayaulymnurtaza/Downloads/lab6/dir-files/demofile.txt', 'r') as file1, open('/Users/ayaulymnurtaza/Downloads/lab6/dir-files/demofile2.txt', 'a') as file2:
  for line in file1:
    file2.write(line)

#task8 удалить файл по указанному пути. Перед удалением проверьте наличие доступа и существует ли данный путь или нет.

path = '/Users/ayaulymnurtaza/Downloads/lab6/dir-files/testfile2.txt'
path_bool = os.access(path, os.F_OK)

if path_bool == False:
    print("Не существует")
    
elif path_bool == True:
    os.remove(path)
    print("Удален")