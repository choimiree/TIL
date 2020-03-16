#A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
#버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
#충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
#만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
#출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

for tc in range(1, int(input())+1):
    K,N,M=map(int,input().split()) #K:이동거리, N:정류장수, M:충전기 수
    pos=[0] + list(map(int,input().split())) + [N]
    bus=ans=0 #bus=현재위치, asn=결과값
    for i in range(1, M+2):
        if pos[i] - pos[i-1] > K:
            ans = 0; break
        if bus + K < pos[i]:
            bus = pos[i-1]
            ans += 1
    print('#{} {}'.format(tc,ans))


#백트레킹 버전
def find(stop, k, cnt):
    global mincnt, K, N, M, scnt

    if stop >= N:
        if cnt < mincnt:
            mincnt = cnt
        return

    if k == 0 and ch[stop] < 1:       # 방전되었는데, 충전이 안 되는 경우
        return                        # 운행종료
    if ch[stop]: scnt += 1  #충전소를 몇 개 지났는지 카우트하기 위함. 뒤에 더이상 충전소가  없을 경우 충전을 하는 경우를 제외시키기 위함.
    if cnt < mincnt:
        if k > 0:
            find(stop+1, k-1, cnt)      # 충전하지 않은 경우
        if ch[stop] and scnt<= M:        # 현재 정류장에서 충전 가능하고, 충전소가 아직 남아 있는 경우
            find(stop+1, K-1, cnt+1)      # 충전한 경우

    return


for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split()) #K:이동거리, N:정류장수, M:충전기 수
    stops = list(map(int, input().split()))

    ch = [0]*(N+1)
    for i in range(M):
        ch[stops[i]] = 1 #현재 정류장 stop이 충전이 가능한지 여부

    mincnt = 999
    scnt = 0 #현재까지 충전소 개수. M은 총충전소 개수
    find(0, K, 0)
    if mincnt == 999: #종점까지 가지 못한 경우
        mincnt = 0
    print(f'#{tc} {mincnt}')