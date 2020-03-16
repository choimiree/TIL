##Sum
#100x100 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
'''
T = 10
for tc in range(1, 11):

    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(100)]

    result = []
    leftcross = 0 #왼쪽위에서 오른쪽 아래로 내려가는 대각선 합
    rightcross = 0 #우른쪽위에서 왼쪽 아래로 내려가는 대각선 합

    for i in range(0, 100):
        linesum = 0 #행의 합은 행이 바뀔 때마다 초기화
        for j in range(0, 100):
            linesum += pan[i][j]
            result.append(linesum)

    for j in range(0, 100):
        rowsum = 0 #열의 합도 열이 바뀔 때마다 초기화
        for i in range(0, 100):
            rowsum += pan[i][j]
            result.append(rowsum)

    for i in range(0, 100):
        leftcross += pan[i][i]
        result.append(leftcross)

    for i in range(0, 100):
        rightcross += pan[i][-i-1]
        result.append(rightcross)

#   result = linesum + rowsum + leftcross + rightcross
    print('#{} {}'.format(tc, max(result)))
'''
## 1259. 금속막대
#원형 금속 막대를 가장 길게 연결하고자 한다. 원형금속 막대는 한 쪽 면에 수나사와 다른 쪽에 암나사로 이루어져 있다.
#수나사와 암나사는 굵기가 서로 다르다. 아래 그림에서 수나사의 굵기는 3을 암나사의 굵기는 4를 나타내고 있다.
#이후 나사의 굵기를 수나사의 굵기x암나사의 굵기로 표현한다. 연결은 +로 한다.
#이와같은 원형 금속 막대를 연결하기 위해서는 수나사의 굵기와 암나사의 굵기가 서로 일치해야 한다.
#예를 들어 두 개의 원형 금속 막대 3x4와 4x5가 있을 때 3x4 + 4x5로 연결되며 4x5 + 3x4로 연결하면 연결되지 않는다.
#수나사와 암나사의 크기가 서로 다른 여러 개의 원형 금속 막대를 가장 많이 연결하려고 한다.
#어떤 순서로 연결해야 가장 많이 연결하는지를 찾는 프로그램을 작성하시오.
'''
T=int(input())
for tc in range(1,T+1):
    N=int(input()) #막대개수
    ls = list(map(int,input().split())) #2N개의 수가 주어짐. 앞에서부터 2개씩 하나의 원형 금속 막대의 수나사 굵기와 암나사 굵기를 의미함.
    new_ls=[]
    bolt=ls[::2]
    nut=ls[1::2]
    for i in range(len(ls)//2):
        for j in range(len(ls)//2):
            if bolt[i] not in nut:
                new_ls.append(bolt[i])
                new_ls.append(nut[i])
                break
    while len(new_ls) != 2*N:
        for s in range(N):
            if new_ls[-1] == bolt[s]:
                new_ls.append(bolt[s])
                new_ls.append(nut[s])
    result = ' '.join(map(str, new_ls))
    print('#{} {}'.format(tc, result))
'''
#지선쓰
# tc = int(input())
# for k in range(1, tc + 1):
#     n = int(input())  # 막대 갯수
#     n_ls = list(map(int, input().split()))
#     m_ls = n_ls[::2]
#     f_ls = n_ls[1::2]
#     new_ls = []
#
#     # 머리
#     for i in range(n):
#         for j in range(n):
#             if m_ls[i] not in f_ls:
#                 new_ls.append(m_ls[i])
#
#
#                 new_ls.append(f_ls[i])
#                 break
#
#     # 머리 뒷부분
#     while len(new_ls) != 2 * n:
#         for s in range(n):
#             if new_ls[-1] == m_ls[s]:
#                 new_ls.append(m_ls[s])
#                 new_ls.append(f_ls[s])
#
#     result = map(str, new_ls)
#
#     print('#{} {}'.format(k, ' '.join(result)))
#용준쓰
# -*- coding: utf-8 -*-
#
# T = int(input())
# for t in range(1, T + 1):
#     n = int(input())
#     n_list = list(map(int, input().split()))
#
#     x_list = []
#     y_list = []
#     for i in range(len(n_list)):
#         if i % 2 == 0:
#             x_list.append(n_list[i])
#         else:
#             y_list.append(n_list[i])
#
#     result_list = []
#
#     for i in range(n):
#         if x_list[i] not in y_list:
#             a = x_list.pop(i)
#             b = y_list.pop(i)
#             result_list.append(a)
#             result_list.append(b)
#             break
#
#     while (len(x_list) > 0):
#         for i in range(len(x_list)):
#             if result_list[-1] == x_list[i]:
#                 a = x_list.pop(i)
#                 b = y_list.pop(i)
#
#                 result_list.append(a)
#                 result_list.append(b)
#                 break
#
#     result = ' '.join(map(str, result_list))
#     print(f'#{t} {result}')
#세경쓰
# case = int(input())
#  
# for i in range(case):
#     result = []
#     num = int(input())
#     bolt = []
#     nut = []
#     k = list(map(int, input().split()))
#     for p in range(0, len(k), 2):
#         bolt.append(k[p])
#         nut.append(k[p+1])
#  
#     for b in bolt:
#         if b not in nut:
#             result.append(b)
#             result.append(nut[bolt.index(b)])
#  
#     while len(result) != len(k):
#          for b in bolt:
#             if result[-1] == b:
#                 result.append(b)
#                 result.append(nut[bolt.index(b)])
#                 break
#  
#     result = list(map(str, result))
#     print('#{} {}'.format(i+1, ' '.join(result)))