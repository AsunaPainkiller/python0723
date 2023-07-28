# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого массива: '))
n_arr = []
while (n>0):
    n_arr.append(int(input('Введите элемент массива: ')))
    n = n-1
m = int(input('Введите количество элементов второго массива: '))
m_arr = []
while (m>0):
    m_arr.append(int(input('Введите элемент массива: ')))
    m = m-1
temp = n_arr[0]
len_n = len(n_arr)
while (len_n>0):
    for i, k in enumerate(n_arr):
        if (n_arr[-1]!=n_arr[i]) and (n_arr[i]>n_arr[i+1]):
            temp = k
            k = n_arr[i+1]
            n_arr[i]=k
            n_arr[i+1]=temp
        elif (n_arr[-1]!=n_arr[i]) and (n_arr[i]==n_arr[i+1]):
            n_arr.pop(i)
    len_n = len_n-1
print(n_arr)
temp = m_arr[0]
len_m = len(m_arr)
while (len_m>0):
    for i, k in enumerate(m_arr):
        if (m_arr[-1]!=m_arr[i]) and (m_arr[i]>m_arr[i+1]):
            temp = k
            k = m_arr[i+1]
            m_arr[i]=k
            m_arr[i+1]=temp
        elif (m_arr[-1]!=m_arr[i]) and (m_arr[i]==m_arr[i+1]):
            m_arr.pop(i)
    len_m = len_m-1
print(m_arr)