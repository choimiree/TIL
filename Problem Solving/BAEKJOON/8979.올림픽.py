'''
어느 국가가 몇등을 했는지 알려면 각국가의 금,은,동 메달 정보를 입력받아서 서로 비교를 해줘야 한다.
근데 여기서 등수를 알고싶은 국가가 정해져있다.
그럼 그 국각의 금,은,동메달과 다른 나라의 금,은,동메달을 비교해주면 된다.
등수를 알고 싶은 국가의 금,은,동메달 갯수가 다른 국가보다 많은지 작은지 각각 비교한다.
시작 cnt를 1로 해서, 등수를 알고 싶은 국가의 메달 갯수가 더 적으면 +1해준다.
'''
N,K=map(int,input().split()) #국가 수, 알고싶은 국가
ls=[list(map(int,input().split())) for _ in range(N)] #국가명, 금 개수, 은 개수, 동 개수
for n in range(len(ls)):
    if ls[n][0] == K:
        Kls = ls[n]
cnt=1
for m in range(len(ls)):
    if ls[m][1] > Kls[1]:
        cnt += 1
    elif ls[m][1] == Kls[1] and ls[m][2] > Kls[2]:
        cnt+=1
    elif ls[m][1] == Kls[1] and ls[m][2] == Kls[2] and ls[m][3] > Kls[3]:
        cnt+=1
print(cnt)
# N,K=map(int,input().split()) #국가의 수, 등수를 알고 싶은 국가
# NKarr= [list(map(int,input().split())) for _ in range(N)]
# # print(NKarr)
# ansK=0
# for i in range(len(NKarr)):
#     if NKarr[i][0] == K:
#         ansK = NKarr[i]    #NKarr[i]가 등수를 알고싶은 국가의 리스트가 된다.
#
# cnt=1 #1등부터 시작하니까. cnt를 프린트해주면 된다.
# for n in range(len(NKarr)):     #ansK의 금은동메달 개수와, 다른 국가의 금은동메달 개수를 비교해준다.
#     if NKarr[n][1] > ansK[1]: #금메달 개수 비교
#         cnt += 1
#     elif NKarr[n][1] == ansK[1] and NKarr[n][2] > ansK[2]:  #은메달 개수 비교
#         cnt += 1
#     elif NKarr[n][1] == ansK[1] and NKarr[n][2] == ansK[2] and NKarr[n][3] > ansK[3]:   #동메달 개수 비교
#         cnt += 1
# print(cnt)