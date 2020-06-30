#0~9까지 숫자가 적힌 N장의 카드가 주어진다.
#가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
#카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
for tc in range(1, int(input())+1):
    N=int(input())
    num=list(map(int, input()))
    cnt=[0]*10
    for i in num:
        #num 리스트에 있는 숫자는 cnt +1
        cnt[i] += 1
    #cnt 수가 많을 수록 카드가 많다는 뜻이므로 최대값이 결과값이 됨.
    result = max(cnt)

    for j in range(len(cnt)):
        if cnt[j] == result:
            a = j
    print('#{} {} {}'.format(tc, a, result))