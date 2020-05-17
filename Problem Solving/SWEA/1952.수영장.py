##[1952. 수영장]
#김프로는 수영장을 이용한다.
# *가장 적은 비용*으로 수영장을 이용하려 한다.
#1일 이용권:1일 이용 가능
#1달 이용권:1달동안 이용 가능. 매달 1일 시작.
#3달 이용권:3달동안 이용 가능. 매달 1일 시작.(11월,12월에도 살 수 있음)
#1년 이용권:1년 동안 이용 가능. 매년 1월 1일 시작.
#3월2일,4월9일,5월1일, 6월5일 이용할 예정.
#각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때, 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램을 작성하라.
#1일이용권 10원, 1달 이용권 40원, 3달 이용권 100원, 1년 이용권 300원.
#시간제한: 최대 50개 테스트 케이스 모두 3초
#모든 종류의 이용권 요금은 10이상 3000이하 정수
#각 달의 이용계획은 각 달의 마지막 일자보다 크지 않다.
def my_cost(k, my_sum):
    global min_cost
    if my_sum > min_cost: #이용권 가격이 연이용권보다 크면 return
        return
    if k >= 12: #(k는 단계라서 0부터 시작) 1년이니까 12달. k가 전체 돌았다는 말. 다 돌고 나서도 이용권 가격이 연이용권보다 저렴하면 min_cost는 my_sum.
        if my_sum < min_cost:
            min_cost = my_sum
        return
    if go[k] == 0: #한 번도 가지 않은 달은 k+1해서 다음 단계로 넘어감.
        my_cost(k+1, my_sum)
    else: #이용권 가격이 연이용권보다 작으면 1일권은 +1해주고 나간횟수*1일권 가격, 1달권은 +1해주고 1달권 가격, 3달권은 +3해주고 3달권 가격.
        my_cost(k+1, my_sum + go[k]*cost[0])#1일권
        my_cost(k+1, my_sum + cost[1])#1달권
        my_cost(k+3, my_sum + cost[2])#3달권

T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    go = list(map(int, input().split())) + [0] #나중에 자릿수 맞춰주려고 [0]추가함
    min_cost = cost[3]
    my_cost(0,0)
    print('#{} {}'.format(tc, my_cost))

'''
#선생님 재귀함수 코드#
def f(n,s,d,m,m3): #s = my_sum
    global minV
    if n>12:
        if minV > s:
            minV = s
    elif minV <= s:
        return
    else:
        f(n+1, s+table[n]*d, d, m, m3) #n월에 1일 이용권
        f(n+1, s+m, d, m, m3) #n월에 1달 이용권
        f(n+3, s+m3, d, m, m3) #n월에 3달 이용권권

for tc in range(1, int(input())+1):
    d, m, m3, y = map(int, input().split()) #이용권비용
    table = [0] + list(map(int, input().split())) #월별이용일
    minV = y #1년 이용권 비용
    f(1, 0, d, m, m3) #1월부터 고려
    print('#{} {}'.format(tc, minV))
'''