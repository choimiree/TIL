#사다리 게임이지겨워진 학생들이 새로운 게임.
# 가위바위보가 그려진카드를 통해 토너먼트로 한 명을 뽑는 것.
# 게임 룰은 1번부터 N번까지 N명의 학생이 N장의 카들르 나눠 갖는다.
# 전체를 두개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 승자가 된다.
# 1은 가위, 2는 바위, 3은 보. 카드 안에 있는게 가위바위보, 카드 밖에 있는게 사람.
#출력: 승자의 번호.
#[배열]활용
def f(i,j):
    if i==j:
        return i
    else:
        r1 = f(i, (i+j)//2)
        r2 = f((i+j)//2+1, j)
        p = [r1, r2]
        return p[w[card[r1]][card[r2]]]
        #return win(r1, r2)

w=[[0],
   [0,0,1,0],
   [0,0,0,1],
   [0,1,0,0]]
T=int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))
    print('#{} {}'.format(tc, f(1,N)))