##[1486.장훈이의 높은 선반]
#서점에는 높이가 B인 선반이 하나 있는데 장훈이는 키가 매우 크기 때문에 선반 위의 물건을 자유롭게 사용할수있다.
#어느날 장훈이는 자리를 비웠고, 이 서점에 있는 N명의 점원들이 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생겼다.
#각 점원의 키는 Hi로 나타나는데, 점원들은 탑을 쌓아서 선반위의 물건을 사용하기로 하였다.
#점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.
#탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.
#탑의 높이가 B이상인 경우 선반 위의 물건을 사용할 수 있는데 탑의 높이가 높을 수록 더 위험하므로 높이가 B이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.

#<부분집합> 코드#
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height_ls = list(map(int,input().split()))
    min = 99 #최소값으로 비교해줘야해서 지정해줌
    for i in range(1, 1<<N): #N개를 다 돌면서 부분 집합 개수 세아려 줌
        sum = 0
        for j in range(N+1):
            if i & (1<<j): #부분집합의 개수 세아려 줌
                sum += height_ls[j] #부분집합을 다 더해 줌
        if sum >= B and sum - B <= min: #부분집합의 합이 선반보다 크고, 부분집합의 합-선반의 높이가 min일 때
            min = sum - B #min = 부분집합의 합 - 선반의 높이
    print('#{} {}'.format(tc, min))

#<재귀함수> 코드#
def back(i, sum): #단계(k), sum
    global min_height
    if sum >= B:
        if sum < min_height:
            min_height = sum
        return
    elif i > N - 1:
        return
    else:
        back(i + 1, sum)
        back(i + 1, sum + height[i])
    return min_height - B

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    min_height = 100000
    result = back(0, 0)
    print('#{} {}'.format(t, result))

