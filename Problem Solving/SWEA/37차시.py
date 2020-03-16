n = int(input())
ls = [1,1]
for i in range(1, n-1):
    ls.append(ls[i-1] + ls[i])
print(ls)