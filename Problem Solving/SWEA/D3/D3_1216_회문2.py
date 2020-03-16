#거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문이라 한다.
#주어진 100x100 글자판에서 가로,세로 모두 보아 가장 긴 회문의 길이를 출력
#각 칸의 들어가는 글자는 c언어 char type으로 주어지면 &apos;A&apos; &apos;B&apos; &apos;C&apos; 중 하나이다.
#글자판은 무조건 정사각형
#가로,세로 각각에 대해서 직선으로만 판단.
import sys
sys. stdin = open("input.txt","r")

T = int(input())
for tc in range(1, T+1):

    arr = [list(map(str, input())) for _ in range(100)]
    ln = []
    #일단 100x100의 행을 탐색
    for i in range(100):
        # ls = []
        #행이 바뀔때마다 리스트를 초기화 시켜줘야하기 때문에 여기 빈 리스트 넣음.
        for j in range(100):
            #한 줄씩 앞에서 읽고, 뒤에서 읽어서 똑같은지 탐색
            #그 대신 시작점이 달라질 수도 있으므로 고려해야함.
            for k in range(100-j+1):
                # 회문이면 그 줄의 각 글자를 한 리스트에 넣음.
                if arr[i][j:j+k] == arr[i][j+k:j-1:-1]:
                    print(arr[i][j:j+k])
                    print(arr[i][j+k:j-1:-1])
                    ln.append(arr[i][j:j+k])
    #열 탐색
    for j in range(100):
        for i in range(100):
            for k in range(100-i+1):
                if arr[j][i:i+k] == arr[j][i+k:i-1:-1]:
                    ln.append(arr[j][i:i+k])
    #길이가 최대로 긴 것 프린트 할랬는데(&apos;int&apos; object is not iterable)떴슴돠.....
    print(max(len(ln)))

    #print(&apos;#{} {}&apos;.format(tc, ))
