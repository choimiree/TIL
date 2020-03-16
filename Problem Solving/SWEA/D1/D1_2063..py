
N = int(input())
P = list(map(int, input().split()))
for i in range(len(P)-1, 0, -1):
    for j in range(0, i):
        if P[j] > P[j+1]:
            P[j],P[j+1] = P[j+1],P[j]
print(P[len(P)//2])




'''
85 72 38 80 69 65 68 96 22
9일때 중간값은 5번째
85 72 38 80 69 65 68 96 22 2 3
11일때 중간값은 6번째
13일때 중간값은 7번째
(n+1)/2
'''
#
# a = int(input())
#
# b = list(map(int, input().split(' ')))
#
# for i in range(len(b) - 1, 0, -1):
#     for j in range(0, i):
#         if b[j] > b[j + 1]:
#             b[j], b[j + 1] = b[j + 1], b[j]
#
# print(b[(len(b) // 2)])