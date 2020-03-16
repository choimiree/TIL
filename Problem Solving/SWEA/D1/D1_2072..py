T = int(input())
for tc in range(1, T+1):

    N = list(map(int, input().split()))

    sum = 0
    for i in N:
        if i % 2 == 1:
            sum += i

    print('#{} {}'.format(tc, sum))
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#
#     result = 0
#     odd_input = list(map(int, input().split()))
#
#     for j in odd_input:
#         if j % 2 == 1:
#             result += j
#
#     print(f'#{test_case} {result}')
