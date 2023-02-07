l = [5, 78, 45, 12, 56, 99]

def nearest(lst, target):
  return min(lst, key=lambda x: abs(x-target))

print(nearest(l, 17))