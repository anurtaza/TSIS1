
#1: умножить все числа в списке
a = [1, 2, 3, 4, 5]

x = '*'.join(str(i) for i in a)
print(eval(x))


#2: принимает строку и вычисляет количество заглавных и строчных букв
txt = input()
cntup = 0
cntlow = 0
for i in txt:
    if i.isupper():
        cntup += 1
    elif i.islower():
        cntlow += 1
print("Uppercase letters: ",cntup)
print("Lowercase letters: ",cntlow)

#3: проверяет, является ли переданная строка палиндромом или нет.
txt = input()
if txt == txt[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")

#4: вызывает функцию квадратного корня через определенные миллисекунды.

import time 
num = int(input())
milsec = int(input())
sec = milsec/1000
time.sleep(sec)
sqrt = num ** 0.5
txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(fnum = num, fsec = milsec, fsqrt = sqrt)
print(txt)

#5:возвращает True, если все элементы кортепа являются истинными.
mytup = (True, True, False)
mytup2 = (True, True, True)
print(all(mytup))
print(all(mytup2))