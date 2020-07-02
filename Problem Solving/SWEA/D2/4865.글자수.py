##4865.글자수
#두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하라.
#예를 들어 str1="ABCA", str2="ABABCA"인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력.
#파이썬의 경우 딕셔너리를 이용할 수 있다.
T =int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    count_lst = [0 for _ in range(len(str1))]
    # print(count_lst)
    for i in str2:
        for j in range(len(str1)):
            if str1[j] == i:
                count_lst[j] += 1
    # print(count_lst)
    max_N = 0
    for k in count_lst:
        if k > max_N:
            max_N = k
    print('#{} {}'.format(tc, max_N))