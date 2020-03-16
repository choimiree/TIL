T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]

    fly_max = []

    for x in range(N-M+1):
        for y in range(N-M+1):
            fly_sum = 0
            for i in range(M):
                for j in range(M):
                    fly_sum += fly_list[x+i][y+j]
                    fly_max.append(fly_sum)

    print('#{} {}'.format(tc, max(fly_max)))













# T = int(input())
# for tc in range(1, T+1):
#
#     N, M = map(int, input().split())
#     fly_list = [list(map(int, input().split())) for _ in range(N)]
#
#     result = []
#     for a in range(N-M+1):
#         for b in range(N-M+1):
#             sum_list = 0
#             for i in range(M):
#                 for j in range(M):
#                     sum_list += fly_list[a+i][b+j]
#                     result.append(sum_list)
#             fly_max=max(result)
#     print('#{} {}'.format(tc, fly_max))



'''
T = int(input())
for tc in range(1, T+1):

    N,M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for a in range(N-M+1):
        for b in range(N-M+1):
            sum = 0
            for i in range(M):
                for j in range(M):
                    sum = sum + fly_list[a+i][b+j]
                    result.append(sum)
    fly_max = max(result)
    print('#{} {}'.format(tc, fly_max))
'''