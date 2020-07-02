'''
세로로 잘리는 위치, 가로로 잘리는 위치 저장을 위한 리스트 생성, 0(시작점)을 미리 넣어둠
가로인지 세로인지에 따라서 가로리스트, 세로리스트에 저장
마지막 점을 리스트에 추가.
가로, 세로 리스트 정렬.(sort)
가로/세로 리스트의 두 점의 거리 (절대값(첫번째-두번째))를 구함.
그 중에서 최대값을 구하고 각각 곱하면 정답.
'''
# N,M=map(int,input().split()) #가로,세로 크기
# dot=int(input()) #점선 개수=자르는 횟수
# Narr=[0]
# Marr=[0]
# for x in range(dot): #세번째줄부터 점선의 개수만큼 있으니까 for문 안에 input을 넣어줘야 합니다.
#     X,Y=map(int,input().split())
#     if X==0:    #가로인지 세로인지에 따라서 가로리스트, 세로리스트에 저장
#         Narr.append(Y)
#     else:
#         Marr.append(Y)
# Narr.append(M)  #마지막 점을 리스트에 추가.
# Marr.append(N)
# Narr.sort() #가로, 세로 리스트 정렬.(sort)
# Marr.sort()
# Nd=0
# Md=0
# Ndmax=-100
# Mdmax=-100
# for i in range(len(Narr)-1):  #가로/세로 리스트의 두 점의 거리 (절대값(첫번째-두번째))를 구함.
#     Nd = abs(Narr[i+1]-Narr[i])
#     if Nd >= Ndmax:   #그 중에서 최대값을 구하고 각각 곱하면 정답.
#         Ndmax = Nd
# for j in range(len(Marr)-1):
#     Md = abs(Marr[j+1]-Marr[j])
#     if Md>=Mdmax:
#         Mdmax = Md
# result = Mdmax * Ndmax    #그 중에서 최대값을 구하고 각각 곱하면 정답.
# print(result)








N,M=map(int,input().split())    #가로길이, 세로길이
Num = int(input())  #점선의 개수
for _ in range(Num):    #점선의 개수만큼 가로(0), 세로(1) 좌표번호
    w, z = map(int,input().split())
    #가로인지 세로인지 판단해서 가로리스트 세로리스트에 넣음
    A = [0] + [N]   #가로리스트
    Mls = [0] + [M] #세로리스트
    #가로리스트에 세로점선
    if w == 1:
        A.append(z)
    else:   #세로리스트에 가로점선 넣는다.
        B.append(z)
    #가로리스트의 인덱스값끼리의 차이가 가장 큰것 찾고
    r=[]
    for i in range(1, len(A)+1):
        r.append(max())
    #세로리스트의 인덱스값끼리의 차이가 가장 큰것 찾아서
    #가로세로길이 곱해주면 가장 큰 넓이 구할 수 있음














