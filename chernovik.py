# from random import random
 
M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int()
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()
 
# for j in range(M):
#     mn = a[0][j]
#     imn = 0    
#     jmn = j
#     for i in range(N):
#         if a[i][j] < mn:
#             mn = a[i][j]
#             imn = i
#     if j == 0 or mn > mx:
#         mx = mn
#         imx = imn
#         jmx = jmn
# print("Максимальный среди минимальных: ", mx)
# print(jmx+1, 'столбец', imx+1, 'строка')

# ---------------------------------------------

# stroki = 3
# stolb = 5
# r = 0  # Чтобы было, чем заполнять
# mas = []
# for i in range(stroki):
#     mas.append([])
#     for j in range(stolb):
#         mas[i].append(r)
#         r = i*j  # Чтобы заполнялось не одно и тоже

# print(mas)
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]