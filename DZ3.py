from random import randint

x = 10
a = []
for i in range(x):
    a.append(randint(1, 99))
print(a)
b = len(a)

for i in range (b):
    f = 0 # ������ �������������� ����������
    for j in range (b-1-i): #�������� i, ����� ������ ��� �� ����������������� �����
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            f = 1
        print(a)
    if f == 0: # ���� ������ ��� ������������, �� ��������� ������ �� ����������
        break
print(a)