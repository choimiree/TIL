# #0~9까지숫자가 적힌 N장의 카드가 주어진다.
# #가장 많은 카드에 적힌 숫자와, 그 카드가 몇 장인지 출력.
# #적힌 숫자가 같을 때는 가장 큰 값을 출력.
'''
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    M = list(map(int, input()))
    cnt = [0] * 10
    for i in M:
        cnt[i] += 1
    result = max(cnt)
    print(cnt)
    print(result)
    for i in range(len(cnt)):
        if cnt[i] == result:
            a = i
    print(a)
    print('#{} {} {}'.format(tc, a, result))
'''
#N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
#M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하라.
'''
T = int(input())
for tc in range(1, T+1):

    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    suml = []
    for i in range(len(arr)-M+1):
        suml.append(sum(arr[i:i+M]))
    result = max(suml) - min(suml)
    print('#{} {}'.format(tc, result))
'''
##[flatten(D3)]
#높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격 줄이는 작업을 평탄화라 한다.
#평탄화를 모두 수행하고 나면, 가장 높은 곳과 낮은 곳의 차이가 최대 1 이내가 된다.
#평탄화를 위해 상자를 옮기는 작업 횟수에 제한이 있을 때, 최고점과 최저점의 차이 반환.
#가장 높은 곳에서 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의.
#가로100 세로 100이하, 덤프 1000이하.
'''
T = 10
for tc in range(10):
N = int(input()) #덤프횟수
h_ls = list(map(int, input().split()))
dump_max = []
dump_min = []

for i in range(len(h_ls)):
    if h_ls[i] == max(h_ls):
        dump_max.append(h_ls[i])

for i in range(len(h_ls)):
    if h_ls[i] == min(h_ls):
        dump_min.append(h_ls[i])

result = dump_max[i] - dump_min[i]

print(result)

T = 10
for tc in range(1, 11):

    dump = int(input())
    nums = list(map(int, input().split()))

    for i in range(dump):
        nums = sorted(nums)
        nums[0] += 1
        nums[-1] -= 1
        if nums[-1] - nums[0] == 1:
            break

    nums = sorted(nums)
    print('#{} {}'.format(tc, nums[-1] - nums[0]))
'''
##[6485.삼성시의버스노선]
#5000개의 버스정류장
#버스노선 N개. i번째 버스노선은 번호가 Ai이상이고 Bi이하인 모든 정류장만 다니는 버스 노선이다.
#P개의 버스정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하라.
#미리쓰
# T=int(input())
# for tc in range(1, T+1):
#     print('#{}'.format(tc),end='')
#
#     N = int(input())
#     for i in range(N):
#         A1, B1 = map(int, input().split())
#         A2, B2 = map(int, input().split())
#
#     busstop = [[0] * 5001]
#     for P in range(5001):
#         P = int(input())
#
#     print('#{} {}'.format())

#정원쓰
# tn = int(input())
# for ir in range(tn):
#     print('#{} '.format(ir+1),end='')
#     N = int(input())
#     A = []
#     B = []
#     for i in range(N):
#         a, b = map(int, input().split())
#         A.append(a)
#         B.append(b)
#     P = int(input())
#     bustop = []
#     for i in range(P):
#         bustop.append(int(input()))
#     print(A)
#     print(B)
#     print(P)
#     print(bustop)
#     re = [0 for i in range(5000)]
#     print(re)
#     for i in range(N):
#         for j in range(A[i]-1, B[i]):
#             re[j] += 1
#     print(i)
#     print(j)
#     print(re)
#     for i in range(P-1):
#         print(re[bustop[i]-1],end=' ')
#     print(re[bustop[-1]-1])

#세경쓰
#########################인덱스 카운트로 풀어서 세경이한테 보ㄴㅐ기!!!!!!!!
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
