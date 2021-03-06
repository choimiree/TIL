#[4837. 부분집합의 합]
#1~12까지 숫자를 원소로 가진 집합 A가 있다.
#집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수
#해당하는 부분집합이 없는 경우 0을 출력.
# A = [1,2,3,4,5,6,7,8,9,10,11,12]
# N = len(A) #원소의 개수(N)를 비트의 길이로 보면 됨
# T = int(input()) #테스트케이스
# for tc in range(1, T+1):
#     temp = list(map(int, input().split())) #N개의 원소와 원소의 합 K를 list로 받을 거임.
#     final_cnt = 0 #집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수 출력해줘야하기 때문에 출력값 설정.
#     for i in range(1<<N): #1을 N만큼 왼쪽으로 밀어서 2^N 안에 있는 2^i만큼 돌리는 것.
#         cnt = 0
#         sum = 0
#         for j in range(N+1): #j는 1~n까지.
#             if i & (1<<j): #&연산은 같은 위치가 1일 때만 1을 말해줌. 즉, j가 001일때, 첫번째 원소를 부분집합으로 가지겠다는 거임. j가 010일때는 010이 나오니까 2번째 원소만 부분집합으로 가지겠다는 것. 011 경우 첫번째,두번째 원소를 부분집합으로 가지겠다는 것.
#                 cnt += 1
#                 sum += A[j]
#         if cnt == temp[0] and sum == temp[1]:
#             final_cnt += 1
#     print('#{} {}'.format(tc, final_cnt))

T=int(input())
for tc in range(1, T+1):
    N,K=map(int,input().split())
    A=[1,2,3,4,5,6,7,8,9,10,11,12]
    final_cnt = 0
    for i in range(1<<N):
        cnt = 0
        sum = 0
        for j in range(N+1):
            if i & (1<<j):
                cnt += 1
                sum += A[j]
        if cnt == N and sum == K:
            final_cnt += 1
    print('#{} {}'.format(tc, final_cnt))