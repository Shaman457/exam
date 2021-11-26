import random
n = 6
m = 6
mat = [[random.randint(1,9) for g in range(m)] for i in range(n)]
print(mat)
a = int(input())
b = int(input())
c = mat[a][b]
print(c)