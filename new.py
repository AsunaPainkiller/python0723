a = int(input('Введите три числа для поиска наибольшего:'))
b = int(input())
c = int(input())

if (a>b):
    if (a>c):
        print('{a} - наибольшее число')
    else:
        print('{c} - наибольшее число')
else:
    print('{b} - наибольшее число')