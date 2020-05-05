##[7일차-행렬찾기]
#창고에는 화학물질용기 n^2개가 n x n으로 배열되어 있었다.
#빈용기에 해당하는 원소는 '0'으로 저장하고, 화학물질의 종류에 따라 '1'에서 '9'사이의 정수를 저장.
#1. 화학물질이 담긴 용기들이 사각형을 이루고 있다. 사각형엔 빈 용기가 없다.
#2. 화학물질이 담긴 용기들로 이루어진 사각형들은 각각 차원이 다르다. A는 3x4, B는 2x3, C는 4x5
#3. 2개의 화학 물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다.
#n은 100 이하.
#부분행렬의 열의 개수는 서로 다르며 행의 개수도 서로 다르다.
#테스트 케이스는 여러개의 그룹으로 구성되며 그룹1~5로 나뉘어져있다.
import sys
sys.stdin = open('0229.txt', 'r')

T = int(input())
for tc in range(1, T+1):
     n = int(input())
     arr = [list(map(int, input().split())) for _ in range(n)]
     r = []
     for x in range(n):
         for y in range(n):
             if arr[x][y] != 0:
                 i = x
                 while arr[i][y] != 0:
                     j = y
                     while arr[i][j] != 0:
                         arr[i][j] = 0
                         j += 1
                     i += 1
                 r.append([i-x, j-y])

     for i in range(len(r)-1):
         for j in range(i+1, len(r)):
             if r[i][0]*r[i][1] > r[j][0]*r[j][1]:
                 r[i],  r[j] = r[j], r[i]
             elif r[i][0]*r[i][1] == r[j][0]*r[j][1]:
                 if r[i][0] > r[j][0]:
                     r[i], r[j] = r[j], r[i]
     print('#{} {}'.format(tc, len(r)),end=' ')
     for k in r:
         print('{} {}'.format(k[0], k[1]), end=' ')
     print()
