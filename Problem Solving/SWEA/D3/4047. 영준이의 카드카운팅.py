##[4047. 영준이의 카드 카운팅]
# 영준이가 하는 카드 게임에는 한 덱의 카드가 필요한데 여기서 얘기하는 "한 덱"이란 스페이드, 다이아몬드, 하트, 클로버 무늬 별로 각각 A, 2~10, J, Q, K의 라벨 즉 4개의 무늬 별로 각각 13장씩 총 52장의 카드가 있는 모음을 의미한다.
# 편의상 A는 1,J,Q,K는 11,12,13으로 하여 1~13의 숫자가 카드에 적혀있다고 하자.
# 영준이는 몇 장의 카드를 이미 가지고 있는데 게임을 하기 위해서 몇 장의 카드가 더 필요한지 알고 싶어 한다.
# 그리고 이미 겹치는 카드를 가지고 있다면 오류를 출력하고자 한다.
# 지금 가지고 있는 카드의 정보가 주어지면 이 작업을 수행하는 프로그램을 작성하라.
T=int(input())
for tc in range(1,T+1):
    str = input()
    ls = []
    for i in range(0,len(str)-2,3):
        ls.append(str[i:i+3])
    S=13
    D=13
    H=13
    C=13
    S_2 = []
    D_2 = []
    H_2 = []
    C_2 = []
    cnt=0
    for j in range(len(ls)):
        if ls[j][0] == 'S':
            if ls[j] in S_2:
                cnt += 1
            else:
                S_2.append(ls[j])
        elif ls[j][0] == 'D':
            if ls[j] in D_2:
                cnt += 1
            else:
                D_2.append(ls[j])
        elif ls[j][0] == 'H':
            if ls[j] in H_2:
                cnt += 1
            else:
                H_2.append(ls[j])
        else:
            if ls[j] in C_2:
                cnt += 1
            else:
                C_2.append(ls[j])
    if cnt != 0:
        print('#{} ERROR'.format(tc))
    else:
        print('#{} {} {} {} {}'.format(tc, S-len(S_2), D-len(D_2), H-len(H_2), C-len(C_2)))
