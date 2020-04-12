#경근이는 알파벳 소문자와 '?'를 사용한 패턴과 매치되는 단어를 찾는 명령을 내릴 수 있는데 '
#"asia"는 이런 패턴에 매치되기는 하지만 팰린드롬이 아니기 때문에 찾아주지는 않고
#입력: 길이가 1이상 20 이하인 문자열, 알파벳 소문자와 ?로 이뤄져 있다.
T=int(input())
for tc in range(1, T+1):
    s=input()
    N=len(s)
    ans = ''
    if N==1:
        ans='Exist'
    else:
        i=0
        # 앞에서 i번째와 끝에서 i번째가 같거나, 둘 중 하나가 '?'인 경우
        while i<N//2 and (s[i]==s[N-1-i] or s[i]=='?'or s[N-1-i]=='?'):
            i+=1    #일치하는 개수
        if i==N//2:
            ans = 'Exist'
        else:
            ans = 'Not exist'
    print('#{} {}'.format(tc,ans))