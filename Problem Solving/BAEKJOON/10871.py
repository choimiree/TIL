#X보다 작은 수

# N개로 이루어진 수열 A와 정수 X가 주어진다.
# 이때 A에서 X보다 작은 수를 출력하라.

N,X=map(int,input().split())
A=list(map(int,input().split()))
ls=[]
for i in range(len(A)):
    if A[i] < X:
        ls.append(A[i])
print(' '.join(map(str, ls)))