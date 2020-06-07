#부분집합
def backtrack(k, hsum):
    global result
    if hsum >= shelf:
        if hsum - shelf < result:   #선반과 키 합의 차이가 최소 차이값보다 작으면 변경
            result = hsum - shelf
            return
    if k == people:
        if hsum >= shelf and hsum - shelf < result:
            result = hsum - shelf
    else:
        backtrack(k+1, hsum+heights[k]) #k번째 점원 포함
        backtrack(k+1, hsum)    #k번째 점원 포함X

for tc in range(int(input())):
    people, shelf = map(int,input().split())
    heights = list(map(int,input().split()))
    result = 999999999999
    if shelf >= sum(heights):   #키를 다 합친 값이 선반보다 작은경우, 바로 계산
        result = shelf - sum(heights)
    else:
        backtrack(0,0)
    print('#{} {}'.format(tc+1, result))