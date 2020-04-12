#덧셈을 배운지 얼마 안 된 준환이는 덧셈에 아직도 어려움을 느낀다.
#그래서 준환이는 N자리인 두 양수를 더하는 연습을 하기로 했다.
#당신은 준환이를 위해 답안지를 만들어주기로했다.
#두 양수가 주어질 때 두 수를 더한 결과를 구하는 프로그램을 작성하라.
#입력: T/ 두 양의 정수 A,B(1<=A,B<10^100)
#출력: A+B
#[참고]
# 뒷자리부터 계산하고, 출력은 앞자리부터.
T=int(input())
for tc in range(1,T+1):
    A,B = input().split()
    lenA = len(A)
    lenB = len(B)
    stack = []
    i = lenA - 1
    j = lenB - 1
    carry = 0   #자리 올림 처음에는 0
    while i >= 0 and j >= 0:
        s = int(A[i]) + int(B[i]) + carry
        carry = s//10
        stack.append(s%10)
        i -= 1
        j -= 1
    while i>=0:
        s=int(A[i]) + carry
        carry = s//10
        stack.append(s%10)
        j -= 1
    if carry != 0:
        stack.append(carry) #9999 + 1인 경우
    print('#{}'.format(tc),end='')
    while stack:
        print(stack.pop(),end='') #stack이 빌 때까지 출력하는 것
    print()