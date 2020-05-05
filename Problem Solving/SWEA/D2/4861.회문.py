# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다.
# NxM 크기의 글자판에서 길이가 M인 회문을 찾아 출력하라.
# 회문은 1개가 존재하는데, 가로뿐만 아니라 세로로 찾아질 수도 있다.
# 입력: 1<=T<=50, 10<=N<=100, 5<=M<=N
## 4861. 회문
#ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN크기의 글자판에서 길이가 M인 회문을 찾아 출력하라.
#회문은 1개가 존재하는데, 가로뿐만아니라세로로 찾아질 수 있따.
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    str_list = [list(input()) for _ in range(N)] #리스트로 뽑았기 때문에 하나씩 문자열로 넣어줘야 슬라이싱 가능.

    for i in range(N):
        str_row ='' #초기화 시켜줘야 i가 바뀔때마다 다시 시작가능
        str_col = ''
        for j in range(N):
            str_row += str_list[i][j] #가로줄 확인
            str_col += str_list[j][i] #세로줄 확인
            if len(str_row) == M: #가로: 길이가 M이 될 때까지 str_list의 원소를 더해줌
                if str_row == str_row[::-1]: #회문일때
                    result = str_row
                else:
                    pass
            if len(str_col) == M:
                if str_col == str_col[::-1]:
                    result =str_col
                else:
                    pass
            #길이탐색 후 멈추면 안되고, 뒤에 남은 것도 구해줘야 됨.
            str_row_back = ''
            str_col_back = ''
            for k in range(j+1, N):
                str_row_back += str_list[i][k]
                str_col_back += str_list[k][i]
                if len(str_row_back) == M:
                    if str_row_back == str_row_back[::-1]:
                        result = str_row_back
                if len(str_col_back) == M:
                    if str_col_back == str_col_back[::-1]:
                        result = str_col_back
    print('#{} {}'.format(tc, result))
'''
def f(N, M):
    for i in range(N):  # 가로회문
        for j in range(N - M + 1):
            for k in range(M // 2):
                if s[i][j + k] != s[i][j + M - 1 - k]:
                    break
                if k == M // 2 - 1:
                    return i, j, 0
        for j in range(N):  # 세로회문
            for i in range(N - M + 1):
                for k in range(M // 2):
                    if s[i + k][j] != s[i + M - 1 - k][j]:
                        break
                    if k == M // 2 - 1:
                        return i, j, 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    s = [input() for i in range(N)]
    i, j, v = f(N, M)
    print('#{}'.format(tc), end=' ')
    if v == 0:
        for h in range(M):
            print(s[i][j + h], end='')
        print()
    else:
        for h in range(M):
            print(s[i + h][j], end='')
        print()
'''