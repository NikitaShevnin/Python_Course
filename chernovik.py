def fun(x):
    for key in dct:
        if x in key:
            return dct.get(key)
 
dct = {
    'AEIOULNSTR' : 1, 'DG' : 2, 'BCMP' : 3,
    'FHVWY' : 4, 'K' : 5, 'JX' : 8, 'QZ' :10
    }
print(sum(map(fun, input())))