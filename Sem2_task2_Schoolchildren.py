# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y 
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать 
# задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

#Вводим основные переменные x&y
print ("Введите x: ", end=' ')
x = int(input())

print ("Введите y: ", end=' ')
y = int(input())

#Подсказака пети сумма и произведение x&y
sum = int (x+y)
prod = int (x*y)

#Катя отвечает
sum_0 = (x-y)
prod_0 = (x/y)

print ("Катин ответ сумма: ", end='')
print (sum_0)
print ("Катин ответ произведение: ", end='')
print (prod_0)