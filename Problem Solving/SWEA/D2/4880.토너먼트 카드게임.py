# 사다리 게임이지겨워진 학생들이 새로운 게임.
# 가위바위보가 그려진카드를 통해 토너먼트로 한 명을 뽑는 것.
# 게임 룰은 1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다.
# 전체를 두개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 승자가 된다.
# 1은 가위, 2는 바위, 3은 보.
# 카드 안에 있는게 가위바위보, 카드 밖에 있는게 사람.
#출력: 승자의 번호.
#[배열]활용

def game(a,b):  #a,b는 카드 정보. 카드의 인덱스값 구해야해서 a,b는 인덱스를 넣은 리스트 형태로 넣어주자.
    #인덱스 [0]값은 그 사람의 번호, [1]은 그 사람의 카드 정보로 설정.
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

#토너먼트, 조 나누기
def tour(arr):
    #마지막으로 게임 가능한 상태로 쪼갰을 때 조건문
    #해당 리스트에 2명만 남았을 때, 최후 단계에서 실행됨
    #현재 정렬이 2명일 때, 즉 가위바위보 게임이 가능할 때
    if len(arr) == 2:
        return game(arr[0], arr[1])
    #현재 정렬에 1명만 남아있을 때, 즉 부전승일 때
    elif len(arr) == 1:
        #그사람 반환
        #한 명밖에 없을 때 유일한 데이터 값인 [0]을 반환
        return arr[0]
    #반반씩 나눠주는 작업. 이를 위해 빈 정렬 두개
    arr1 = []
    arr2 = []
    for i in range(len(arr)):
        #앞에 반 개를 arr1에 넣어줌
        if i <= (len(arr)-1)//2:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    #계속 반으로 쪼개고 쪼개고 쪼개기 위해, 결국 가위바위보를 2명만 하게 하기 위해
    #재귀로 이 함수 반복시켜줌
    return game(tour(arr1), tour(arr2))

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    cards = list(map(int,input().split()))
    #input에서 받은 카드 데이터를 '인덱스==그사람의 번호'와 같이 담아주기 위해 데이터 재정비
    idx = 1
    cards_idx = []
    for card in cards:
        cards_idx.append([idx, card])
        idx += 1
    #결과는 이긴사람의 카드정보 [그사람의 번호, 그사람의 카드 번호]로 나온다.
    result = tour(cards_idx)
    #따라서 그 사람의 번호인 result[0]가 답
    print('#{} {}'.format(tc, result[0]))


