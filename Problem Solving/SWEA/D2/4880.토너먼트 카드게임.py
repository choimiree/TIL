# 사다리 게임이지겨워진 학생들이 새로운 게임.
# 가위바위보가 그려진카드를 통해 토너먼트로 한 명을 뽑는 것.
# 게임 룰은 1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다.
# 전체를 두개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 승자가 된다.
# 1은 가위, 2는 바위, 3은 보. 카드 안에 있는게 가위바위보, 카드 밖에 있는게 사람.
#출력: 승자의 번호.
#[배열]활용

#1=가위, 2=바위, 3=보
def win(p1,p2):
    if card[p1]==card[p2]:
        return p1
    elif card[p1]==2 and card[p2]==1:
        return p1
    elif card[p1]==3 and card[p2]==2:
        return p1
    elif card[p1]==1 and card[p2]==3:
        return p1
    else:
        return p2

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))
    # print(card)

    #단계1: 조 나누기
    while len(card) > 3:


    print('#{} {}'.format(tc, )

'''
원빈쓰 코드

def game(a, b):
    if a[1] == b[1]:
        return a

    if a[1] == 1:
        if b[1] == 2:
            return b
        elif b[1] == 3:
            return a
    
    elif a[1] == 2:
        if b[1] == 1:
            return a
        elif b[1] == 3:
            return b
    
    elif a[1] == 3:
        if b[1] == 1:
            return b
        elif b[1] == 2:
            return a

def tour(arr):
    if len(arr) == 2:
        return game(arr[0], arr[1])
    elif len(arr) == 1:
        return arr[0]

    arr1 = []
    arr2 = []

    for i in range(len(arr)):
        # if arr[i][0] <= (arr[0][0] + arr[len(arr)-1][0])//2: # 아래와 같은 코드
        if i <= (len(arr) - 1) // 2:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    
    return game(tour(arr1), tour(arr2))

for case in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    
    idx = 1
    cards_idx = []
    for card in cards:
        cards_idx.append([idx, card])
        idx += 1

    result = tour(cards_idx)
    
    print(f'#{case} {result[0]}')
    '''