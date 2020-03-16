## String-4864.문자열비교
#두개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
#예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
'''
T=int(input())
for tc in range(1, T+1):
    N=input()
    M=input()

    result = 0
    for i in range(len(M)-len(N)+1):
        if M[i:i+len(N)] == N:
            result += 1
    print('#{} {}'.format(tc, result))
'''
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

##4865.글자수
#두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개 수를 출력하라.
#예를 들어 str1="ABCA", str2="ABABCA"인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력.
#파이썬의 경우 딕셔너리를 이용할 수 있다.
'''
T =int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    count_lst = [0 for _ in range(len(str1))]
    for i in str2:
        for j in range(len(str1)):
            if str1[j] == i:
                count_lst[j] += 1
    max_N = 0
    for k in count_lst:
        if k > max_N:
            max_N = k
    print('#{} {}'.format(tc, max_N))
'''


