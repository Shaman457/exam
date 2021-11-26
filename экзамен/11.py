dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
c = {i:g for i,g in dic.items() if g%2==0}
m = {}
print(c)