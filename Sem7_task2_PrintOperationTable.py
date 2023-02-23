# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру 
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и 
# столбцов таблицы, которые должны быть распечатаны. 
# Ввод:     
# print_operation_table(lambda x, y: x * y) 
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18    
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# ---------------------------------------------

# Заполнение списков
stroki = 6
stolb = 6
r = 1  # накопитель
list_a = []     # с каждой новой строки он должен начинать всё сначала!
for i in range (stroki):
    list_a.append([])
    for j in range (stolb):
        list_a[i].append(r)
        r = i*j  # Задать порядок и шаг заполнения списков за счет произведения элементов
        print(list_a[i][j], end=' ')
    print ()

# 99
# функция которая находит элемент по номеру строки и столбца.
def operation (num_rows, num_columns):
    print ("Введите строку: ", end=' ')
    num_rows = int(input())
    print ("Введите столбец: ", end=' ')
    num_columns = int(input())
    print ('Элемент согласно вашего запроса: ', list_a [num_rows][num_columns])
