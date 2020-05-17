def isRun(arr):
    for i in range(8):
        if arr[i] > 0 and arr[i + 1] > 0 and arr[i + 2] > 0:
            return True
    return False

def playGame():
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(12):
        if i & 1 == 0:
            player1[card[i]] += 1
            if player1[card[i]] == 3:
                return 1
            if isRun(player1):
                return 1
        else:
            player2[card[i]] += 1
            if player2[card[i]] == 3:
                return 2
            if isRun(player2):
                return 2
    return 0  # 무승부

T = int(input())
for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    winner = playGame()
    print('#{} {}'.format(tc, winner))