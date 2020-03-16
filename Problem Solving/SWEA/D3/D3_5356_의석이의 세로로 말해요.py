T = int(input())
for tc in range(1, T+1):

    lst = []
    max_len = 0
    for i in range(5):
        N = input()
        if len(N) > max_len:
            max_len = len(N)
        lst.append(N)

    answer = ''
    for i in range(max_len):
        for j in range(5):
            if len(lst[j]) != 0:
                answer += lst[j][0]
                lst[j] = lst[j][1:]

    print('#{} {}'.format(tc, answer))


