#두 개의 문자열 str1과 str2가 주어진다.
#문자열 str1에 포함된 글자들이 str2에 몇개씩 들어있느지 찾고, 그중 가장 많은 글자의 개수를 출력.
#예를 들어 str1="ABCA", str2="ABABCA"인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
#딕셔너리 이용할 수 있다.
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    dict = {}.fromkeys(str1, 0) #dictionary 생성

    for ch in str2:
        if ch in dict:
            dict[ch] += 1

    print('#{} {}'.format(tc,max(dict.values())))

#counting으로 푸는 방법
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = [0] * 128 #문자를 배열의 인덱스로 사용한다.
    for ch in str2:
        cnt[ord(ch)] += 1

    ans = 0
    for ch in str1:
        if cnt[ord(ch)]:
            ans = max(ans, cnt[ord(ch)])
            