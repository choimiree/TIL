#[6485.삼성시의버스노선]
#5000개의 버스정류장
#버스노선 N개. i번째 버스노선은 번호가 Ai이상이고 Bi이하인 모든 정류장만 다니는 버스 노선이다.
#P개의 버스정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하라.

#세경쓰
#인덱스 카운트로 풀어서 세경이한테 보ㄴㅐ기!!!!!!!!
# for i in range(int(input())):
#     b_stop = [0 for _ in range(5001)]
#     for go in range(int(input())):
#         A, B = list(map(int, input().split()))
#         for b in range(A, B + 1):
#             b_stop[b] += 1
#
#     P = int(input())
#     result = [0 for _ in range(P)]
#     for p in range(P):
#         result[p] = b_stop[int(input())]
#     print('#{} {}'.format(i + 1, ' '.join(map(str, result))))

#소람쓰
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    busline = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    busstop_num = []
    for i in range(P):
        busstop_num.append(int(input()))
    busstop = []
    for i in range(len(busline)):
        for j in range(2):
            a = busline[i][0] #정류장의 시작번호 a
            b = busline[i][1] #정류장의 끝번호 b 받을 예정
        for k in range(a, b+1):
            busstop.append(k) #a~b에 해당하는 모든 정류장번호를 받을 예정
    cnt_list = []
    for i in busstop_num:
        cnt = 0
        for j in range(len(busstop)):
            if i == busstop[j]:
                cnt += 1
        cnt_list.append(cnt)
    result = ' '.join(map(str, cnt_list))
    print('#{} {}'.format(tc, result))
'''
