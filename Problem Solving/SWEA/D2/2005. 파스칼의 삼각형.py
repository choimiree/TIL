
##[2005. 파스칼의 삼각형]
# 파스칼의 삼각형은 아래와 같은 규칙을 따른다.
# 1. 첫번째 줄은 항상 숫자 1이다.
# 2. 두번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
# N이 4일 경우,
#   1
#  1 1
# 1 2 1
# 1 3 3 1
# 파스칼의 삼각형의 크기 N은 1이상 10이하의 정수이다.

# T =int(input())
# for tc in range(1,T+1):
#     N=int(input())
#     print('#{}'.format(tc))
#     pascal = [[1] * i for i in range(1,N+1)]
#     # print(pascal)
#     for j in range(2, len(pascal)):
#         for k in range(1, len(pascal[j])-1):
#             pascal[j][k] = pascal[j-1][k-1] + pascal[j-1][k]
#     for m in range(N):
#         for n in range(len(pascal[m])):
#             print(pascal[m][n], end=' ')
#         print()


T=int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N=int(input())
    pascal = [[1]*i for i in range(1, N+1)]
    # print(pascal)
    for j in range(2, len(pascal)):
        for k in range(1, len(pascal[j])-1):
            pascal[j][k] = pascal[j-1][k-1] + pascal[j-1][k]
            # print(pascal)
    for m in range(N):
        for n in range(len(pascal[m])):
            print(pascal[m][n], end=' ')
        print()














