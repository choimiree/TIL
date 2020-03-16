# [4836. 색칠하기]
# T = int(input())
# for tc in range(1, T+1):
#
#     paint_num = int(input())
#     paint_in2 = [[0] * 10 for _ in range(10)]
#     cnt = 0
#     for k in range(paint_num):
#         temp = list(map(int, input().split()))
#         for i in range(10):
#             for j in range(10):
#                 if i >= temp[0] and i <= temp[2]:
#                     if  j>= temp[1] and j <= temp[3]:
#                         # 색이 겹칠떄(이미 색이 들어와 있다면 )어떻게 처리할지
#                         if paint_in2[i][j] == 1 or paint_in2[i][j] == 2:
#                             cnt += 1
#                         else:
#                             paint_in2[i][j] = temp[4]
#     print('#{} {}'.format(tc, cnt))

#[4837. 부분집합의 합]
#1~12까지 숫자를 원소로 가진 집합 A가 있다.
#집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수
#해당하는 부분집합이 없는 경우 0을 출력.
A = [1,2,3,4,5,6,7,8,9,10,11,12]
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    final_cnt = 0
    for i in range(len(A)):
        if i
#[7일차-행렬찾기]
#창고에는 화학물질용기 n^2개가 n x n으로 배열되어 있었다.
#빈용기에 해당하는 원소는 '0'으로 저장하고, 화학물질의 종류에 따라 '1'에서 '9'사이의 정수를 저장.
#1. 화학물질이 담긴 용기들이 사각형을 이루고 있다. 사각형엔 빈 용기가 없다.
#2. 화학물질이 담긴 용기들로 이루어진 사각형들은 각각 차원이 다르다. A는 3x4, B는 2x3, C는 4x5
#3. 2개의 화학 물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다.
#n은 100 이하.
#부분행렬의 열의 개수는 서로 다르며 행의 개수도 서로 다르다.
#테스트 케이스는 여러개의 그룹으로 구성되며 그룹1~5로 나뉘어져있다.
# T = int(input())
# for tc in range(1, T+1):
#
#     TC = int(input())
#     arr = [list(map(int, input().split())) for _ in range(TC)]
#     print(arr)
