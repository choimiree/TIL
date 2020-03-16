#아이디어
#7자리 숫자가 만들어지면 set에 추가해 중복을 제거한다.
#set의 크기를 출력한다.
T=int(input())
for tc in range(1,T+1):
    a = [list(map(int,input().split())) for i in range(4)]
    t = set()
    for i in range(4):
        for j in range(4):
            find(i,j,0,'')
    print('#{} {}'.format(tc, len(t)))
