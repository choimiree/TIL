#영준이는 학생들의 시험을 위해 N개의 문제를 만들었다.
#각 문제의 배점은 문제마다 다를 수 있고, 틀리면 0점 맞으면 배점만큼의 점수를 받게 된다.
#학생들이 받을 수 있는 점수로 가능한 경우의 수는 몇 가지가 있을까?
#예를 들어, 첫 번째 Testcase의 경우, 총 문제의 개수는 3개이며 각각의 배점은 2,3,5점이다.
#가능한 시험점수의 경우의 수를 살펴보면 0,2,3,5,7,8,10의 7가지가 있다.
#두번째 testcase의 경우, 총 문제의 개수는 10개이며 각각의 배점은 모두 1점이다.
#가능한 시험점수의 경우의 수를 살펴보면 0,1,2,3,4,5,6,7,8,9,10으로 모두 11가지이다.
T=int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(map(int,input().split())) #문제별 점수
    ans = set([0]) #0점인 경우
    #set: 중복제거

    for x in p:
        num = set()
        for y in ans:
            num.add(x+y)
        ans = set(list(ans)+list(num))
    print('#{} {}'.format(tc, len(set(ans))))

