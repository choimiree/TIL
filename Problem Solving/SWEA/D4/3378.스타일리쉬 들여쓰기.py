'''
스타일리쉬 프로그래밍 언어: 알파벳, 세 종류의 괄호 문자, 온점('.') 그리고 개행으로 이루어져 있다.
괄호는 소괄호 (), 중괄호 {}, 대괄호 []로 이뤄져 있고 서로 짝이 잘 맞도록 써야한다.
일반적인 언어에서의 괄호를 사용하는 법과 같다.
스타일리쉬는 다른 언어들과는 다르게 공백을 사용하지 않고 들여쓰기를 표현한다.
들여쓰기가 잘 된 스타일리쉬 코드는 각 괄호가 등장한 횟수에 따라 들여쓰기를 하는 정도가 달라지게 되는데,
1<=R,C,S<=20을 만족하는 세 정수 R,C,S에 대해 이전 줄에서 소괄호가 짝이 맞지 않는 개수만큼 R번씩,
(를 a, )를 b, {를 c, }를 d, [를 e, ]를 f라고 하면 그 줄을 들여쓰기 해야 하는 칸 수는
R(a-b)+C(c-d)+S(e-f)가 된다.
'''
def A_F(code, l):
    global af
    ab = 0  #(-)
    cd = 0  #{-}
    ef = 0  #[-]
    for i in range(len(code[i])):
        if code[i][j] == '(':
            ab += 1
        elif code[i][j] == ')':
            ab -= 1
        elif code[i][j] == '{':
            cd += 1
        elif code[i][j] == '[':
            ef += 1
        elif code[i][j] == ']':
            ef -= 1
    af.append((ab, cd, ef)) #괄호의 차 저장

def RCS(af, indenp, p):
    org = []
    ab, cd, ef = af[0]
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                if p == 1:
                    org.append((R,C,S)) #모든 값이 후보
                elif R * ab + C * cd + S * ef == indenp[1]:
                    org.append((R,C,S))
    for i in range(2,p):
        ab, cd, ef = af[i-1]
        dest = []
        for R, C, S in org:
            if R * ab + C * cd + S * ef == indenp[i]:
                dest.append((R,C,S))
        org = dest
    return org

T=int(input())
for tc in range(1, T+1):
    p,q = map(int,input().split())
    indenp = [0]*p  #들여쓰기 온점 개수 기록

    codep = []
    codeq = []

    for i in range(p):
        codep.append(input())
    for i in range(q):
        codeq.append(input())
    af = []
    A_F(codep, p)   #괄호 개수

    for i in range(p):  #들여쓰기 개수 확인
        cnt = 0
        while codep[i][cnt] == '.':
            cnt += 1
        indenp[i] = cnt

    #R,C,S 후보 정하기
    rcs = RCS(af, indenp, p)

    af = [] #라인별 괄호 개수
    A_F(codeq, q)
    indenq = [0]*q
    for i in range(1, q):
        ab, cd, ef = af[i-1]    #이전 줄 까지의 괄호수
    if rcs:
        R, C, S = rcs[0]
        ans = R*ab + C*cd + S*ef
        for x in rcs[1:]:
            R,C,S = x
            if R*ab + C*cd + S*ef != ans:
                indenq[i] = -1
                break
        if indenq[i] != -1:
            indenq[i] = ans
        else:
            indenq[i] = -1
            break
    print('#{}'.format(tc), end='')
    for x in indenq:
        print(x, end='')
    print()

