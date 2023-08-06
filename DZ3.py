from random import randint

x = 10
a = []
for i in range(x):
    a.append(randint(1, 99))
print(a)
b = len(a)

for i in range (b):
    f = 0 # вввели дополнительную переменную
    for j in range (b-1-i): #добавили i, чтобы проход был по неотсортированной части
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            f = 1
        print(a)
    if f == 0: # если список уже отсортирован, то следующий проход не происходит
        break
print(a)