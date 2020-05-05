##[6190. 정곤이의 단조 증가하는 수]
#정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했따.
#그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
#어떤 k자리 수 X=d1d2...dk가 d1<=d2<=...<=dk를 만족하면 단조 증가하는 수이다.
#예를들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
#양의 정수 N개 A1,...,AN이 주어진다.
#1<=i<j<=N인 두 i,j에 대해, Ai x Aj 값이 단조 증가하는 수인 것들을 구하고, 그 중의 최댓값을 출력하는 프로그램을 작성하라.
#용준쓰코드
T=int(input())
for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int, input().split()))
    result = -1
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            a = ls[i]*ls[j]
            n = str(a)
            cnt = 0
            for x in range(len(n)-1):
                if n[x] <= n[x+1]:
                    cnt += 1
                else:
                    break
            if cnt == len(n)-1:
                if int(n) > result:
                    result = int(n)
    print('#{} {}'.format(tc, result))