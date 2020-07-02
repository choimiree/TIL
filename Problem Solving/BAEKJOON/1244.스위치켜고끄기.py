'''
1은 스위치가 켜져 있음, 0은 꺼져 있음을 나타낸다.
남학생: 스위치 번호가 자기가 받은 수의 배수이면, 스위치의 상태를 바꾼다.
여학생: 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
학생수는 100이하인 양의 정수이다.
남자 1, 여자 2
'''
# # N = int(input()) #스위치개수
# # Sw = [0] + list(map(int,input().split())) #스위치상태
# # #1번 인덱스부터 저장하고 싶을 때
# # M=int(input()) #학생수
# # for _ in range(M):
# #     gender, num = map(int,input().split())
#     if gender == 1: #남자
#         #num의 배수에 해당하는 스위치를 변경
#         for i in range(num, N+1, num):
#             #Sw[i] ^= 1
#             if Sw[i]==1:
#                 Sw[i] = 0
#             else:
#                 Sw[i] = 1
#     # else:           #여자
#     #     if Sw[num]==1:
#     #         Sw[num]=0
#     #     else:
#     #         Sw[num]=1
#     #     l, r = num - 1, num + 1
#     #     while l >= 1 and r <= N:
#             if Sw[l] != Sw[r]:
#                 break
#             if Sw[l]==1:
#                 Sw[l] = 0
#             else:
#                 Sw[l] = 1
#             if Sw[r]==1:
#                 Sw[r] = 0
#             else:
#                 Sw[r] =1
#             l, r = l-1, r+1
# # for i in range(1, N + 1, 20):   # 주의: 1번 부터 출력하기
# #     print(' '.join(map(str, Sw[i: i + 20])))

N=int(input())  #스위치개수
arr = [0] + list(map(int,input().split()))    #스위치의 상태: 켜짐 1 꺼짐 0
Num=int(input())    #학생수
for _ in range(Num):
    gender, cnt = map(int,input().split()) #남 1, 여 2
    if gender == 1: #남자
        #스위치 번호가 자기가 받은 수의 배수이면, 스위치 상태 바꾼다.
        for i in range(cnt, N+1, cnt):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    else:   #여자 #일단 받은 번호의 자리부터 바꿔줌
        if arr[cnt]==1:
            arr[cnt]=0
        else:
            arr[cnt]=1
        #받은 번호의 왼쪽, 오른쪽 대칭인지 판단.
        l, r = cnt - 1, cnt + 1
        # 왼쪽, 오른쪽 범위는 1~N 사이임.
        while 1 <= l and r <= N:
            if arr[l] != arr[r]:
                break
            if arr[l] == 1:
                arr[l] = 0
            else:
                arr[l] = 1
            if arr[r] == 1:
                arr[r] = 0
            else:
                arr[r] = 1
            l, r = l-1, r+1

for r in range(1, N+1, 20):
    print(' '.join(map(str, arr[r:r+20])))






