# 그룹단어체커

#연속해서 나타날 경우만 그룹단어라 체크
# 알파벳 소문자로만 되어있고 중복되지 않는다.

N=int(input())
#총 몇개의 단어가 그룹단어인지 판단하기위한 카운팅 초기값 설정
cnt = 0
#단어 N개 있으니까 N개 탐색
for n in range(1, N+1):
    #첫번째 단어 A 리스트에 넣어서 한개씩 분해했어
    A=list(map(str,input()))
    # print(A)
    # 스펠링 중복안되는지 판단하기위해 일단 빈리스트 만들었어
    ls=[]
    ls.append(A[0])
    for i in range(1, len(A)):
        #전 스펠링이랑 비교해서 다르면 넣어줘야하는데
        if A[i-1] != A[i]:
            # 스펠링이 다르긴 한데 이미 ls에 있으면 안됨, break
            if A[i] in ls:
                break
            else:
                ls.append(A[i])
    else:
        #단어 한개 탐색 끝나면 cnt +=1 해주고 다음 단어 탐색
        cnt += 1
# 그룹단어 갯수 출력
print(cnt)

