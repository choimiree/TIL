#0~9까지숫자가 적힌 N장의 카드가 주어진다.
#가장 많은 카드에 적힌 숫자와, 그 카드가 몇 장인지 출력.
#적힌 숫자가 같을 때는 가장 큰 값을 출력.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input()))
    cnt = [0] * 10
    for i in M:
        cnt[i] += 1
    result = max(cnt)
    print(cnt)
    print(result)
    for i in range(len(cnt)):
        if cnt[i] == result:
            a = i
    print(a)
    print('#{} {} {}'.format(tc, a, result))

'''
#N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
#M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하라.
'''
T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    suml = []
    for i in range(len(arr)-M+1):
        suml.append(sum(arr[i:i+M]))
    result = max(suml) - min(suml)
    print('#{} {}'.format(tc, result))