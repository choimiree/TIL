#V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
#두 개의 노드에 대해 경로가 있으면 1, 없으면 0 출력.
#노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있따.
def

T=int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) #V는 노드개수, E는 간선 개수.
    arr = [list(map(int,input().split())) for _ in range(E)] #E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보 주어짐.
    S, G = map(int,input().split()) #출발노드S, 도착노드G

    print('#{} {}'.format(tc, result))
    #출력하는 법 모르겠음: 노드에 경로가 있으면 1, 없으면 0 출력.
