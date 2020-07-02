#A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
#버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
#충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
#만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
#출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
T=int(input())
for tc in range(1, T+1):
    #최대이동할 수 있는 정류장 수K, N번 정류장까지, 충전기설치 정류장 M개
    tlist=list(map(int,input().split()))
    #M개의 충전소 위치
    Mlist = list(map(int,input().split()))

    def elbus(tlist, mlist):
        #노선별 K,N,M
        K=tlist[0]
        N=tlist[1]
        M=tlist[2]

        if len(mlist) != M:
            return '충전기 수와 설치된 정류장 수가 일치하지 않습니다.'

        #차고지와 종점 위치 포함 리스트
        flist = list(Mlist)
        flist.append(N)
        flist.insert(0,0)

        #먼저 충전소가 잘못 설치된 경우 생각
        #충전소 간의 거리는 이동거리=K를 넘어서는 안된다.
        for i in range((len(flist)-1)):
            if flist[i+1] - flist[i] > K:
                return 0
        count = 0
        #마지막 정거장부터 뒤에서 정거장을 꺼내서 '이동 가능한 가장 뒤에 있는 정거장(l)'을 추출
        #거리=정거장위치(l)-내위치(s) <= K면 이동 가능
        #이동 후 나의 위치는 해당 정거장(l)의 위치

        #나의 현재 위치
        current_location = 0

        for s in flist:
            # s=출발하는 정류장이 종점이면 for문 종료
            if s == N:
                break
            #이동한 정거장(변경된 나의 위치)에서 출발
            if s == current_location:
                for l in flist[::-1]:
                    if l - s <= K:
                        #l=종점이면 충전 불필요
                        if l == N:
                            break

                        current_location = l
                        count += 1
                        break

        return count

    print('#{} {}'.format(tc, elbus(tlist, Mlist)))


# #백트레킹 버전
# def find(stop, k, cnt):
#     global mincnt, K, N, M, scnt
#
#     if stop >= N:
#         if cnt < mincnt:
#             mincnt = cnt
#         return
#
#     if k == 0 and ch[stop] < 1:       # 방전되었는데, 충전이 안 되는 경우
#         return                        # 운행종료
#     if ch[stop]: scnt += 1  #충전소를 몇 개 지났는지 카우트하기 위함. 뒤에 더이상 충전소가  없을 경우 충전을 하는 경우를 제외시키기 위함.
#     if cnt < mincnt:
#         if k > 0:
#             find(stop+1, k-1, cnt)      # 충전하지 않은 경우
#         if ch[stop] and scnt<= M:        # 현재 정류장에서 충전 가능하고, 충전소가 아직 남아 있는 경우
#             find(stop+1, K-1, cnt+1)      # 충전한 경우
#
#     return
#
#
# for tc in range(1, int(input())+1):
#     K, N, M = map(int, input().split()) #K:이동거리, N:정류장수, M:충전기 수
#     stops = list(map(int, input().split()))
#
#     ch = [0]*(N+1)
#     for i in range(M):
#         ch[stops[i]] = 1 #현재 정류장 stop이 충전이 가능한지 여부
#
#     mincnt = 999
#     scnt = 0 #현재까지 충전소 개수. M은 총충전소 개수
#     find(0, K, 0)
#     if mincnt == 999: #종점까지 가지 못한 경우
#         mincnt = 0
#     print(f'#{tc} {mincnt}')