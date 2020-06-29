#forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이  3 4 +. ('.'은 출력하라는 뜻)
#forth에서 동작은 다음과 같다.
#숫자는 스택에 넣는다.
#연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
# '.'은 스택에서 숫자를 꺼내 출력한다.
# 형식이 잘못되면 'error'출력
#1. 연산자 만나면 두개 빼서 연산자 처리하고 push
#2. 연산자 만났을 때 두개가 아니면 error

def f():
    s = []
    for i in range(len(code)):
        if code[i]=='+' or code[i]=='-' or code[i]=='/' or code[i]=='*':
            if len(s) >= 2:
                op2 = int(s.pop())
                op1 = int(s.pop())
                if code[i] == '+':
                    s.append(op1+op2)
                elif code[i]=='-':
                    s.append(op1-op2)
                elif code[i]=='*':
                    s.append(op1*op2)
                elif code[i]=='/':
                    s.append(op1//op2)
            else: #if len(s) < 2:
                return 'error'
        elif code[i]!='' and code[i]!='.':  #숫자면..
            s.append(code[i])
        elif code[i] == '.':
            if len(s) == 1:
                return s.pop()
            else:
                return 'error'


T = int(input())
for tc in range(1, T+1):
    code = list(input().split())

    print('#{} {}'.format(tc, f()))

