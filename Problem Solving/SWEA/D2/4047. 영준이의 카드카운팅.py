#딕셔너리 사용하는 방법
dict = {'S':0, 'D':1, 'H':2, 'C':3}
for tc in range(1, int(input())+1):
    arr = input()
    #필요한 카드 개수
    cnt = [13]*4  #0번: 스페이드, ... 3번: 클로바, 무늬별로 필요한 카드 수
    check = [[0] * 13 for _ in range(4)] #행값: 무늬, 열값:라벨(숫자)
    for i in range(0, len(arr), 3):
        a = dict[arr[i]]
        b = int(arr[i+1]) * 10 + int(arr[i+2])
        if check[a][b]:
            print('ERROR');
            break  # ERROR
        check[a][b] = 1
        cnt[a] -= 1
    else:
        print(cnt)

# T = int(input())
# for tc in range(1, T+1):
#
#     str = input()
#     lst = []
#     for i in range(0, len(str)-2, 3):
#         lst.append(str[i:i+3])
#
#     space = 13
#     dia = 13
#     hart = 13
#     clover = 13
#     s_2 = []
#     d_2 = []
#     h_2 = []
#     c_2 = []
#     cnt = 0
#
#     for j in range(len(lst)):
#         if lst[j][0] == 'S':
#             if lst[j] in s_2:
#                 cnt += 1
#             else:
#                 s_2.append(lst[j])
#         elif lst[j][0] == 'D':
#             if lst[j] in d_2:
#                 cnt += 1
#             else:
#                 d_2.append(lst[j])
#         elif lst[j][0] == 'H':
#             if lst[j] in h_2:
#                 cnt += 1
#             else:
#                 h_2.append(lst[j])
#         elif lst[j][0] == 'C':
#             if lst[j] in c_2:
#                 cnt += 1
#             else:
#                 c_2.append(lst[j])
#
#     if cnt != 0:
#        print('#{} {}'.format(tc, 'ERROR'))
#     else:
#         print('#{} {} {} {} {}'.format(tc, space-len(s_2), dia-len(d_2), hart-len(h_2), clover-len(c_2)))
