#문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이 부분을 다시 지운다.
#반복문자를 지운 후 남은 문자열의 길이를 출력하시오. 남은 문자열이 없으면 0을 출력.
#입력: 첫 줄 1<=T<=50, 다음 줄 길이 1000이내인 문자열
#출력: stack에 남아있는 글자수 출력
#아이디어
# 빈 stack 만들어서, 다음 글자와 stack의 맨 위 글자를 비교해서 같으면 pop(), 다르면 push()
T = int(input())
for tc in range(1, T+1):
    s = input()
    top = -1    #가장 마지막으로 저장된 원소의 인덱스
    stack = [0]*1000    #최대 글자수만큼 지정
    top += 1 #push
    stack[top] = s[0] #push
    for i in range(1, len(s)):
        if stack[top]==s[i]:
            top -= 1
        else:
            top += 1
            stack[top] = s[i]
    print('#{} {}'.format(tc, top+1))   #stack이 비어있으면 인덱스가 -1이 되기때문에 +1을 해줘야한다.


