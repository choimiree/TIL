#충전기를 교환하는 방식의 전기버스를 운행하려한다.
#정류장에는 교체용 충전지가 있는 교환기가 있고,충전지마다 최대로 운행할 수 있는 정류장이 있따.
#충전기가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도달해야 한다.
#정류장과 충전지에 대한 정보가 주어질때, 목적지에 도착하는데 필요한 <<최소한의 교환 횟수를 출력>>
#<<단, 출발지에서 배터리 장착은 교환횟수에서 제외한다.>>

#첫줄에 테스트케이스 수 1<=T<=50
#다음줄부터 한줄에 정류장수 N, N-1개의 정류장 별 배터리 용량 Mi(3<=N<=100,0<Mi<N)
#각 줄마다 "#T"를 출력한 뒤, 답 출력

'''
각각의 정류장에서 배터리를 교환할지말지!가 선택지.
배터리가 없을 때는 무조건 교환하는걸로 처리.
경우의 수 줄일 수 있다.
'''
def backtrack(idx,remain,cnt):
    global N, min, stops
    remain -= 1 #다음정류장 도착하면 배터리 감소
    if idx == N:
        if cnt < min:
            min = cnt
        return
    if cnt > min:
        return
    #배터리를 교환하고 다음 정류장으로 진행
    backtrack(idx+1, stops[idx], cnt+1)
    #배터리를 교환하지 않고 다음 정류장으로 진행
    if remain > 0:
        backtrack(idx+1, remain, cnt)

T=int(input())
for tc in range(1,T+1):
    stops = list(map(int,input().split()))
    N = stops[0]    #정류장의 개수
    min = 10000
    backtrack(2,stops[1],0) #시작인덱스는 2번!
    print('#{} {}'.format(tc, min))


















