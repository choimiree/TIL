#input 수가 주어지면
n= num = int(input())
#cnt초기값
cnt = 0
#똑같은 수 나올때까지 반복
while True:
    #각자리수를 구해서
    ten = int(n//10)
    one = int(n%10)
    #더한다
    plus = ten+one
    cnt += 1
    n = int(str(n%10)+str(plus%10))
    if n == num:
        break
print(cnt)
