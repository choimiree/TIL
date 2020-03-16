#조합
# N=3
# for i in range(N-1): # i = 0부터 N-2까지
#     for j in range(i+1, N): #
#         print(i,j)

for tc in range(1, int(input())+1):
    N=int(input())
    arr=list(map(int, input().split()))
    arr.sort(reverse=True)
    #N개의 값들에서 2개 선택해서 곱하는 모든 경우
    ans = -1 #가장 큰 값을 저장하기위해 변수 지정. 곱하기라 1이상임.
    for i in range(N-1):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            if ans >= num: break
            t = num #계속 나머지와 나누기 연산을 해야하기 때문에 변수 지정.
            b = t%10 #1의 자리
            t = t//10 #t는 몫
            while t:
                a=t%10
                if a>b: break
                t //= 10 #t=몫
                b = a #1의 자리는 t를 10으로 나눈 나머지가 됨
            else:           #단조증가하는 수
                ans = max(ans, num)
    print(ans)

            #곱하기 결과가 단조 증가하는 수인지 판단

    #출력시 단조증가하는 경우가 없으면 -1을 출력
