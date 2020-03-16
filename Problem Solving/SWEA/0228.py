#[4837. 부분집합의 합]
#1~12까지 숫자를 원소로 가진 집합 A가 있다.
#집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수
#해당하는 부분집합이 없는 경우 0을 출력.
'''
A = [1,2,3,4,5,6,7,8,9,10,11,12]
N = len(A) #원소의 개수(N)를 비트의 길이로 보면 됨
T = int(input()) #테스트케이스
for tc in range(1, T+1):
    temp = list(map(int, input().split())) #N개의 원소와 원소의 합 K를 list로 받을 거임.
    final_cnt = 0 #집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수 출력해줘야하기 때문에 출력값 설정.

    for i in range(1<<N): #1을 N만큼 왼쪽으로 밀어서 2^N 안에 있는 2^i만큼 돌리는 것.
        cnt = 0
        sum = 0
        for j in range(N+1): #j는 1~n까지.
            if i & (1<<j): #&연산은 같은 위치가 1일 때만 1을 말해줌. 즉, j가 001일때, 첫번째 원소를 부분집합으로 가지겠다는 거임. j가 010일때는 010이 나오니까 2번째 원소만 부분집합으로 가지겠다는 것. 011 경우 첫번째,두번째 원소를 부분집합으로 가지겠다는 것.
                cnt += 1
                sum += A[j]
        if cnt == temp[0] and sum == temp[1]:
            final_cnt += 1

    print('#{} {}'.format(tc, final_cnt))
'''

##[4839. 이진탐색]
#짝을 이룬 A,B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이긴다.
#예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 I=1, 오른쪽 r=400이 되고, 중간 페이지 c=int((I+r)/2)로 계산한다.
#찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
#A는 300, B는 50쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른쪽 영역의 중간 페이지를 다시 찾아가면 된다.
#책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하라.
#비긴경우는 0을 출력.
'''
T=int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    result = []
    for i in range(2):
        start = 1
        end = temp[0]
        page = temp[i+1]
        cnt = 0
        while start <= end:
            mid = (start+end)//2
            if mid == page:
                break
            elif mid < page:
                start = mid
                cnt += 1
            else:
                end = mid
                cnt += 1
        result.append(cnt)

    if result[0] < result[1]:
        print('#{} A'.format(tc))
    elif result[0] > result[1]:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))
'''
##[4843. 특별한정렬]
#보통 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
#N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
#예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
#10 1 9 2 8 3 7 4 6 5
#주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오.
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    New_Ai = sorted(Ai)
    result = []
    while len(result) < 10:
        result.append(New_Ai.pop(-1))
        result.append(New_Ai.pop(0))
    print(result)
    final_result = ' '.join(map(str, result))
    print('#{} {}'.format(tc, final_result))
'''