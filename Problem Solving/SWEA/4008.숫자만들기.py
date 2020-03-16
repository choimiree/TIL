#4008.숫자만들기
# N개의 숫자가 적혀있는게임판이 있고 + - x / 의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구해보기로 했따.
#수식을 계산할 때 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산한다.
#예를 들어 1,2,3이 적힌 게임 판에 +와 x를 넣어 1+2*3을 만들면 1+2를 먼저 계산하고 그 뒤에 *를 계산한다.
#주어진 연산자 카드를 사용하여 수식을 계산했을 때 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하시오.
#시간제한: 최대 50개 3초
#게임 판에 적힌 숫자의 개수 N은 3이상 12이하의 정수
#연산자 카드 개수의 총 합은 항상 N-1
#게임 판에 적힌 숫자는 1이상 9이하 의 *정수*
#수식을 완성할 때 각 연산자 카드를 모두 사용
#숫자와 숫자 사이에는 연산자가 1개만 들어가야 한다.
#완성된 수식을 계산할 때 연산자의 우선순위는 고려하지 않고, 왼쪽에서 오른쪽으로 차례대로 계삲나다.
#*나눗셈을 계산할 때 소수점 이하는 버린다.* => 절대값으로 나눗셈을 한 다음 다시 부호를 붙여야 함.
#입력으로 주어지는 숫자의 순서는 변경할 수 없다.
#연산 중의 값은 -100,000,000 이상 100,000,000이하임이 보장된다.

def max_min(k, m_sum, a,b,c,d): #k:단계(N까지),
   global s_max, s_min
   if k == N:#가지 끝났다 -> 값 비교 #재귀함수 끝날 수 있는 조건
       if m_sum <= s_min:
           s_min = m_sum
       if m_sum >= s_max:
           s_max = m_sum
       # return
   else: #가지가 안 끝났을 때 (k가 N이 될때까지)
       if a>0: #+
          max_min(k+1, m_sum+n_list[k], a-1, b,c,d)
       if b>0: #-
          max_min(k+1, m_sum-n_list[k], a, b-1, c, d)
       if c>0: #*
          max_min(k+1, m_sum*n_list[k], a, b, c-1, d)
       if d>0: #/
          max_min(k+1, int(m_sum/n_list[k]), a, b, c, d-1)
   return s_max-s_min


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    a,b,c,d=map(int, input().split())
    n_list = list(map(int,input().split()))
    s_max = -100000000
    s_min = 100000000
    result = max_min(1,n_list[0],a,b,c,d)
    print('#{} {}'.format(tc, result))
'''
def f(n, k, r, op1, op2, op3, op4):
    global minV, maxV
    if n==k:
        if maxV<r:
            maxV = r
        if minV>r:
            minV = r
    else:
        if op1>0:
            f(n+1, k, r+card[n], op1-1, op2, op3, op4)
        if op2>0:
            f(n+1, k, r-card[n], op1, op2-1, op3, op4)
        if op3>0:
            f(n+1, k, r*card[n], op1, op2, op3-1, op4)
        if op4>0:
            f(n + 1, k, int(r/card[n]), op1, op2, op3, op4 - 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a,b,c,d = map(int, input().split())
    n_list = list(map(int, input().split()))
    s_max = -10000000000
    s_min = 10000000000
    f(1, N, card[0], op1, op2, op3, op4)
    print('#{} {}'.format(tc, maxV-minV))
'''