# 이진 트리에서 임의의 두 정점의 공통 조상 중 가장 가까운 것을 찾으려 한다.
# 임의의 이진 트리가 주어지고, 두 정점이 명시될 때 이들의 공통 조상 중 이들에 가장 가까운정점을  찾고, 그 정점을 루트로 하는 서브트리의 크기를 알아내는 프로그램을 작성하라.

T=int(input())
for tc in range(1, T+1):
    V,E,num1,num2 = list(map(int,input().split())) #정점총수,간선총수,정점1,정점2
    PC= list(map(int,input().split()))  #E개의 간선 나열(부모/자식)
    P=PC[i][0]
    C=PC[i][1]
    parent=0
    subtree=0

    print('#{} {} {}'.format(tc, parent, subtree))