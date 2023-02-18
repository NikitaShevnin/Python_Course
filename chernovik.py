res = 0
lst = [1, 9, -15, 24, 17, -4, -7, 2, 31, 16, -7, 11, 44, 21, -12]
p = int(input()) -1
q = int(input()) -1
for i, x in enumerate(lst):
    if p <= i <= q : 
        res += x
print(res)